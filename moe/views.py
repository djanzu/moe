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
        context =  super().get_context_data(**kwargs)
        kiroku = models.Kiroku.objects.all().order_by('dt')
        old_moyori = 0
        old_moe = 0
        out = []
        for i in kiroku:
            diff_moyori = 0 if old_moyori == 0 else int(i.moyori_cnt) - old_moyori
            diff_moe = 0 if old_moe == 0 else int(i.moe_cnt) - old_moe
            old_moyori = i.moyori_cnt
            old_moe = i.moe_cnt
            out.append({
                "dt": i.dt,
                "moyori_cnt": int(i.moyori_cnt),
                "moe_cnt": int(i.moe_cnt),
                "diff_moyori": diff_moyori,
                "diff_moe": diff_moe,
            })
        context['datas'] = out
            
        return context

    def get_queryset(self):
        return models.Kiroku.objects.all().order_by('-dt')  
