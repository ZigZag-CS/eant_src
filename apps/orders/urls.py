# -*- coding: utf-8 -*-
from django.urls import path, re_path

from .views import *

app_name = "orders"

urlpatterns = [

    path('', OrderListView.as_view(), name='list'),

    re_path(r'^(?P<order_id>[0-9A-Za-z]+)/$', OrderDetailView.as_view(), name='detail'),

# re_path(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', AccountEmailActivateView.as_view(), name='email-activate'),

]