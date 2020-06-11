from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<slug:slug>/', ProductDetailSlugView.as_view()),
]
