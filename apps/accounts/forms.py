# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm pass", widget=forms.PasswordInput)

    # validator daca username exista
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)

        if qs.exists():
            raise forms.ValidationError("Username exists")

        return username

    # validator daca username exista
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)

        if qs.exists():
            raise forms.ValidationError("Email exists")

        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password2 != password:
            raise forms.ValidationError("Password error")

        return data
