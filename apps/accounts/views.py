from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.generic import CreateView, FormView, DetailView
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import *
from .models import *
from .signals import user_logged_in


User = get_user_model()


# @login_required # /accounts/login/?next=/some/path/
# def account_home_view(request):
#     return render(request, "accounts/home.html", {})


#LoginRequiredMixin,
class AccountHomeView(LoginRequiredMixin, DetailView):

    template_name = 'accounts/home.html'

    def get_object(self):
        return self.request.user




def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email       = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")
    return redirect("/register/")


class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        # print(f"pana la email: {form.cleaned_data} ")
        email  = form.cleaned_data.get("username")
        # print(f"email: {email} ")
        password  = form.cleaned_data.get("password")
        # print(f"password: {password} ")
        # print(f"request: {request} ")
        user = authenticate(request, username=email, password=password)
        # print(f"pana la {user} :")
        if user is not None:
            if not user.is_active:
                messages.error(request, 'This user is inactive')
                return super(LoginView, self).form_invalid(form)
            login(request, user)
            user_logged_in.send(user.__class__, instance=user, request=request)
            try:
                del request.session['guest_email_id']
            except:
                print(" tipa passs")
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(form)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'



# def login_page(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     # print(request.user.is_authenticated)
#     next_ = request.GET.get('next')
#     next_post = request.POST.get('next')
#     redirect_path = next_ or next_post or None
#     if form.is_valid():
#         # print(form.changed_data)
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(request, username=username, password=password)
#         # print(user)
#         # print(request.user.is_authenticated)
#         if user is not None:
#             # print(request.user.is_authenticated)
#             login(request, user)
#             try:
#                 del request.session['guest_email_id']
#             except:
#                 pass
#             if is_safe_url(redirect_path, request.get_host()):
#                 return redirect(redirect_path)
#             else:
#                 return redirect("/")
#         else:
#             # Return daca login e invalid, mesaj de eroare
#             print("Error")
#     return render(request, "accounts/login.html", context)
#
#
# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         # print(form.changed_data)
#         # username = form.cleaned_data.get("username")
#         # email = form.cleaned_data.get("email")
#         # password = form.cleaned_data.get("password")
#         # new_user = User.objects.create_user(username, email, password)
#         # print(f'new user: {new_user}')
#         form.save()
#     return render(request, "accounts/register.html", context)
#
