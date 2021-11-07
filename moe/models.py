from django.db import models
from django.utils import timezone

class Sengakuji(models.Model):
    dt = models.DateTimeField(default=timezone.now)
    cnt = models.IntegerField()

    def __str__(self):
        return self.cnt


class Moework(models.Model):
    dt = models.DateTimeField(default=timezone.now)
    cnt = models.IntegerField()

    def __str__(self):
        return self.cnt
    