from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from apps.products.models import *

class SearchProductView(ListView):
    template_name = 'search/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_disct = request.GET
        query = method_disct.get('q', None)
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()

