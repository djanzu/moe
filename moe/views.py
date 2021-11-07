from django.shortcuts import render
from . import models

# Create your views here.

class KirokuView(generic.ListView):
    # login_url = '/app/login/'
    template_name = 'moe/kiroku_list.html'
    models = models.Moe
    paginate_by = 25

