from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return HttpResponse("Hello, world. You're at todos/ index.")


def make(request):
  return HttpResponse("Make Todos")