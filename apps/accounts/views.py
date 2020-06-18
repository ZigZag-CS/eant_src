from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import *

User = get_user_model()


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    # print(request.user.is_authenticated)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        # print(form.changed_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        # print(user)
        # print(request.user.is_authenticated)
        if user is not None:
            # print(request.user.is_authenticated)
            login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            # Return daca login e invalid, mesaj de eroare
            print("Error")
    return render(request, "accounts/login.html", context)


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.changed_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(f'new user: {new_user}')
    return render(request, "accounts/register.html", context)

