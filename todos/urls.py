from django.urls import path
from . import views

urlpatterns = [
    path('create_todo/', views.create_todo, name="addTodo"),
    path('edit_todo/', views.edit_todo, name="edit_todo"),
    path('lookup_todo/<int:id>/', views.dynamic_view, name="spesific_todo"),
    path('delete_todo/<int:id>/', views.delete_todo, name="delete_todo"),
    path('', views.index, name="index"),
]
