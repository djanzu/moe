# loaddataでやりたかったけどうまく行かなかったｗ

import datetime
# from django.utils import timezone
# from tzlocal import get_localzone
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from moe import models

class Command(BaseCommand):
    def handle(self, *args, **options):
        # ja = get_localzone()
        x = [
            {"dt": "2021/11/03 19:26", "moyori": 29616, "moe": 10333},
            {"dt": "2021/11/04 19:51", "moyori": 29637, "moe": 10390},
            {"dt": "2021/11/05 20:41", "moyori": 29662, "moe": 10453},
            {"dt": "2021/11/06 21:06", "moyori": 29726, "moe": 10521},
            {"dt": "2021/11/07 19:19", "moyori": 29777, "moe": 10572},
            {"dt": "2021/11/08 20:30", "moyori": 29812, "moe": 10628},
        ]
        for i in x:
            dt = datetime.datetime.strptime(i['dt'], '%Y/%m/%d %H:%M')
            dt_aware = make_aware(dt)
            kiroku_obj = models.Kiroku(dt=dt_aware, moyori_cnt=i['moyori'], moe_cnt=i['moe'])
            kiroku_obj.save()
