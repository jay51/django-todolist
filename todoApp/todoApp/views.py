from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Auth
# For authenticating users
from django.contrib.auth import authenticate


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("/")

        return HttpResponse("Wrogn email or password")

    # Return an 'invalid login' error message.
    return render(request, "todoApp/login.html")


# if request.user.is_authenticated:
#     # Do something for authenticated users.
# else:
#     # Do something for anonymous users.


def logout_view(request):
    logout(request)
    return redirect("/")
#     # Redirect to a success page.


def signup(request):
    if request.user.is_authenticated:
        return HttpResponse("your loged in ")
        # Note:
        # pass the form a long name and a valid long password for form to submit
    if request.method == "POST":
        # SIGNUP user
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("post request")
            form.save()
            # grap user's username and password for authentication
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            # authenticate will auth user and hash password
            user = authenticate(request, username=username,
                                password=raw_password)

            login(request, user)
            return redirect("/")

        # RETURN form
    form = UserCreationForm()
    return render(request, "todoApp/signup.html", {"form": form})


def index_page(request):
    return render(request, "todoApp/index.html")
