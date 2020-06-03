from django.shortcuts import render


def index(request):
    return render(request, "myapp/index.html")

def register(request):
    return render(request, "myapp/register.html")

def home(request):
    return render(request, "myapp/home.html")