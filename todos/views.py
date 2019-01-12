from .form import AddTodo
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todos
# from todoapp.settings import SECRET_KEY


# Create your views here.
def index(request):
    print(f"\n {request.method}\n")
    todos = Todos.objects.all()
    context = {
        "title": "Todos",
        "todos": todos,
    }
    return render(request, "index.html", context)


def create_todo(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        form = AddTodo(request.POST)
        # Validate Data
        if form.is_valid():
            form.save()

            return redirect("/todos")

    # if a GET (or any other method) we'll create a blank form
    else:
        initial_data = {
            "Todo": "Your Todo",
            "summery": "Your summery",
            "done": True
        }
        form = AddTodo(initial=initial_data)
        return render(request, "create_todo_form.html", {"form": form})


def edit_todo(request):
    # first todo in DB
    todo = Todos.objects.get(id=1)
    # give the todo to form to poupliate form with data
    form = AddTodo(request.POST or None, instance=todo)
    # when submit
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "edit_todo.html", {"form": form})


def dynamic_view(request, id):
    # fetch todo by id from DB
    # todo = Todos.objects.get(id=id)
    todo = get_object_or_404(Todos, id=id)

    return render(request, "lookup_todo.html", {"todo": todo})


def delete_todo(request, id):
    todo = Todos.objects.get(id=id)

    if request.method == "POST":
        todo.delete()

    return redirect("/todos")
