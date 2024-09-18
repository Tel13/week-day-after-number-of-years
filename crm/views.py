from django.shortcuts import render, redirect
from .forms import CreateUsersForm,LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# nu lasam un user neutentificat sa acceseze pagina de login
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request, 'crm/index.html')

def register(request):
    form = CreateUsersForm()
    if request.method == "POST":
        form = CreateUsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my_login")

    context = {'registerform':form}

    return render(request, 'crm/register.html', context=context)

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return  redirect("dashboard")

    context = {"loginform":form}

    return render(request, 'crm/my_login.html', context=context)

@login_required(login_url="my_login") # ca sa nu lasam un uzer neautentificat sa acceseze pagina
def dashboard(request):
    return render(request, 'crm/dashboard.html')

def user_logout(request):
    auth.logout(request)
    return redirect("")