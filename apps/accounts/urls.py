# -*- coding: utf-8 -*-
from django.urls import path, re_path

from .views import *

app_name = "account"

urlpatterns = [

    path('', AccountHomeView.as_view(), name='home'),

    re_path(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', AccountEmailActivateView.as_view(), name='email-activate'),

    path('email/resend-activation/', AccountEmailActivateView.as_view(), name='resend-activation'),

]