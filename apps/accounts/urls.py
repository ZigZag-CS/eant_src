# -*- coding: utf-8 -*-
from django.urls import path

from .views import *

app_name = "account"

urlpatterns = [
    path('', AccountHomeView.as_view(), name='home'),
]