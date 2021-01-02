from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UserForm, UserSignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def register_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get("password1") == form.cleaned_data.get("password2"):
                get_user = User.objects.filter(email=form.cleaned_data.get("email"))
                if not get_user:
                    user = User.objects.create_user(
                        username=form.cleaned_data.get("username"),
                        email=form.cleaned_data.get("email"),
                        password=form.cleaned_data.get("password1")
                    )
                    user.save()
                    login(request, user)
                    return redirect('/')
    return render(request, template_name='auth/register.html', context={})

def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get("username"), password=form.cleaned_data.get("password"))
            print(form.cleaned_data.get("username"))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    return render(request, template_name='auth/login.html', context={})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')
