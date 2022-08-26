from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Главная</h2>")


def hello_user(request):
    message = request.GET.get("message")
    name = request.GET.get("name")
    return HttpResponse(f"<h2>Hello {name}! {message}!</h2>")
