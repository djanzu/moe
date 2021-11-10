import datetime
import math
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.utils.timezone import make_aware
from django.db.models import Avg, Min, Max
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

        # 過去７日間
        kako7 = datetime.datetime.now() - datetime.timedelta(days=7)
        # kiroku_ave = models.Kiroku.objects.filter(dt__gt=make_aware(kako7)).aggregate(ave_moyori_cnt=Avg('moyori_cnt'), ave_moe_cnt=Avg('moe_cnt'))
        kiroku2 = models.Kiroku.objects.filter(dt__gt=make_aware(kako7)).aggregate(
            min_moyori_cnt=Min('moyori_cnt'), 
            max_moyori_cnt=Max('moyori_cnt'), 
            min_moe_cnt=Min('moe_cnt'),
            max_moe_cnt=Max('moe_cnt'),
            max_dt=Max('dt'),
            min_dt=Min('dt')
            )
        diff_moyori = kiroku2['max_moyori_cnt'] - kiroku2['min_moyori_cnt']
        diff_moe = kiroku2['max_moe_cnt'] - kiroku2['min_moe_cnt']
        diff_dt = kiroku2['max_dt'] - kiroku2['min_dt']
        ave_moyori = diff_moyori / diff_dt.days
        ave_moe = diff_moe / diff_dt.days
        left_day_moyori = math.ceil((50000 - kiroku2['max_moyori_cnt']) / ave_moyori)
        left_day_moe3 = math.ceil((30000 - kiroku2['max_moe_cnt']) / ave_moe)
        left_day_moe5 = math.ceil((50000 - kiroku2['max_moe_cnt']) / ave_moe)
        reach_moyori = make_aware(datetime.datetime.now() + datetime.timedelta(days=left_day_moyori))
        reach_moe3 = make_aware(datetime.datetime.now() + datetime.timedelta(days=left_day_moe3))
        reach_moe5 = make_aware(datetime.datetime.now() + datetime.timedelta(days=left_day_moe5))
        context['otherdata'] = {
            "left_day_moyori": left_day_moyori,
            "left_day_moe3": left_day_moe3,
            "left_day_moe5": left_day_moe5,
            "ave_moyori": math.floor(ave_moyori),
            "ave_moe": math.floor(ave_moe),
            "reach_moyori": reach_moyori,
            "reach_moe3": reach_moe3,
            "reach_moe5": reach_moe5,
        }

        return context

    def get_queryset(self):
        return models.Kiroku.objects.all().order_by('-dt')  


class AjaxWriteView(generic.FormView):
    def post(self, request, *args, **kwargs):
        print(request.POST)
        """ save data """
        input_dt = request.POST.get("dt", "").replace("-", "/")
        if input_dt != "":
            dt = datetime.datetime.strptime(input_dt, '%Y/%m/%d %H:%M')
        else:
            dt = datetime.datetime.now()
        dt_aware = make_aware(dt)
        kiroku_obj = models.Kiroku(
            dt=dt_aware,
            moyori_cnt=request.POST.get('moyori').replace(",", ""),
            moe_cnt=request.POST.get('moe').replace(",", ""))
        kiroku_obj.save()

        return JsonResponse({
            "stat": "OK",
            "dt": dt_aware
            })
