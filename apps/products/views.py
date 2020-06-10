from django.views.generic import ListView
from django.shortcuts import render

from .models import *

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(f'Context: {context}')
    #     return context


