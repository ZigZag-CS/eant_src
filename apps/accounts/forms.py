# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.safestring import mark_safe

from .models import *

User = get_user_model()



class ReactivateEmailForm(forms.Form):
    email       = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = EmailActivation.objects.email_exists(email)
        if not qs.exists():
            register_link = reverse("register")
            msg = """This email does not exists, would you like to <a href="{link}">register</a>?
            """.format(link=register_link)
            raise forms.ValidationError(mark_safe(msg))
        return email



class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email', ) #'full_name',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'is_active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]



class GuestForm(forms.Form):
    email    = forms.EmailField()


class LoginForm(forms.Form):
    username = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)


# seamana oleaka cu UserAdminCreationForm
class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm pass", widget=forms.PasswordInput)

    # validator daca username exista
    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     qs = User.objects.filter(username=username)
    #
    #     if qs.exists():
    #         raise forms.ValidationError("Username exists")
    #
    #     return username

    # validator daca username exista
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     qs = User.objects.filter(email=email)
    #
    #     if qs.exists():
    #         raise forms.ValidationError("Email exists")
    #
    #     return email

    # def clean(self):
    #     data = self.cleaned_data
    #     password = self.cleaned_data.get("password")
    #     password2 = self.cleaned_data.get("password2")
    #
    #     if password2 != password:
    #         raise forms.ValidationError("Password error")
    #
    #     return data

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        # print(self.cleaned_data)
        user.set_password(self.cleaned_data["password"])
        user.is_active = False  # send confirmation email
        if commit:
            user.save()
        return user


    class Meta:
        model = User
        fields = ('full_name', 'email',)  # 'full_name',)
