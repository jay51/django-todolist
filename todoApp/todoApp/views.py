from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import TodoForm


# Auth
# For authenticating users
from django.contrib.auth import authenticate


def login_view(request):
    # if user got redirect to login from a protected route,
    # django save that route in next query
    next = request.GET.get("next")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            if next:
                return redirect(next)
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


@login_required(login_url="/signin")
def index_page(request):
    return render(request, "todoApp/index.html")


@login_required(login_url="/signin")
def create_todo_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TodoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TodoForm()

    return render(request, 'todoApp/create_todo.html', {'form': form})
