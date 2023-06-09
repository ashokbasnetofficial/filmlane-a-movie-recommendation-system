from django import forms
from django.shortcuts import redirect, render

from accounts.forms import LoginForm,RegisterForm
from .forms import LoginForm
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# Create your views here.
# user login here 
def login_User(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(type(username))
         
            user = authenticate(request,username = username,password = password)
         
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('movies:index')

            else:
                form.add_error(None,'Invalid Credentials')

            

    return render(request,'accounts/login.html',{'form':form})


# user registration method 
def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.password = make_password(instance.password)
            instance.save()

            # form.save()
            return redirect('login')

    
    return render(request,'accounts/register.html',{'form':form})


@login_required(login_url='login')

def logout_user(request):
    logout(request)
    return redirect('movies:index')


    