from django.db import models


class DataItem(models.Model):

    moment = models.DateTimeField()
    offset = models.BigIntegerField()
    key = models.CharField(max_length=1024)
    value = models.FloatField(null=True)
