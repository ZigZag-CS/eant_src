from django.urls import path
from .views import *


app_name = "search"

urlpatterns = [
    path('', SearchProductView.as_view(), name="query"),

]