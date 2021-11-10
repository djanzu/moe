from django.db import models
from django.utils import timezone

class Kiroku(models.Model):
    dt = models.DateTimeField(default=timezone.now)
    moyori_cnt = models.IntegerField()
    moe_cnt = models.IntegerField()

    # def __str__(self):
    #     return self.cnt

class Mokuhyo(models.Model):
    last_moyori = models.IntegerField()
    last_moe = models.IntegerField()
