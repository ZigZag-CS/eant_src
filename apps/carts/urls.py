from django.urls import path
from .views import *


app_name = "carts"

urlpatterns = [
    path('', cart_home, name="home"),
    path('update/', cart_update, name="update"),
    path('checkout/', checkout_home, name='checkout'),
]
