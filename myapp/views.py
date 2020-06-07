from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        
        if user is not None :
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "username or password incorrect")
    return render(request, 'myapp/index.html')


def register(request):
    if request.method == 'GET':
        return render(request, "myapp/register.html", {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('index')
        else:
            return render(request, "myapp/register.html", {'form': UserCreationForm(), 'error': 'username or password incorrect'})

def logoutpage(request):
    logout(request)
    return redirect('index')

@login_required
def home(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user= request.user
            fs.save()
        return redirect('home')
    context = {
        'tasks': Task.objects.all(),
        'form' : form,
    }
    return render(request, "myapp/home.html", context)