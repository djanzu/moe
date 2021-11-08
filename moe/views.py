from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.

class KirokuView(generic.ListView):
    # login_url = '/app/login/'
    template_name = 'moe/kiroku_list.html'
    models = models.Kiroku
    paginate_by = 25

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return models.Kiroku.objects.all().order_by('-dt')  
