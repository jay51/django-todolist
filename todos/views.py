from .form import AddTodo
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo


# Create your views here.
def index(request):
    print(f"\n {request.method}\n")
    # pull all todos from DB
    todos = Todo.objects.all()
    context = {
        "title": "Todos",
        "todos": todos,
    }
    return render(request, "index.html", context)


def create_todo(request):
    # if a POST request we need to process the form data
    if request.method == "POST":
        # create a form with the posted data
        form = AddTodo(request.POST)
        # Validate Data
        if form.is_valid():
            form.save()

            return redirect("/todos")

    # if a GET request (or any other method) we'll create a blank form
    else:
        initial_data = {
            "Todo": "Your Todo",
            "summery": "Your summery",
            "done": True
        }
        form = AddTodo(initial=initial_data)
        return render(request, "create_todo_form.html", {"form": form})


# This will break if you delete the first todo in DB
#  You need to pass todo id from urls.py and look for todos by id in DB
def edit_todo(request):
    # first todo in DB
    todo = Todo.objects.get(id=1)
    # give the todo to form to poupliate form with data
    form = AddTodo(request.POST or None, instance=todo)
    # if form submit
    if request.method == "POST":
        if form.is_valid():
            # save data to DB
            form.save()
    return render(request, "edit_todo.html", {"form": form})

# id is passed from urls.py


def dynamic_view(request, id):
    # fetch todo by id from DB
    # todo = Todos.objects.get(id=id)
    todo = get_object_or_404(Todo, id=id)

    return render(request, "lookup_todo.html", {"todo": todo})

# Delete todo by id. Accepts only post requests


def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    # delete and redirect to home page
    if request.method == "POST":
        todo.delete()

    return redirect("/todos")
