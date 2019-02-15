from django.shortcuts import render, redirect
# Auth
# For authenticating users

from django.contrib.auth import authenticate
# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.

# if request.user.is_authenticated:
#     # Do something for authenticated users.
# else:
#     # Do something for anonymous users.


from django.contrib.auth import logout, login

# def logout_view(request):
#     logout(request)
#     # Redirect to a success page.


from django.contrib.auth.forms import UserCreationForm


def signup(request):
    # Note:
    # Make you pass the form a long name and a valid long password for form to submit
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
