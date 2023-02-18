from django.db import models


class DataItem(models.Model):

    moment = models.DateTimeField()
    offset = models.BigIntegerField()
    key = models.CharField(max_length=1024)
    value = models.FloatField(null=True)


class Signal(models.Model):

    name = models.CharField(max_length=1024)
    formula = models.TextField()
    min_alert_value = models.FloatField(null=True, blank=True)
    max_alert_value = models.FloatField(null=True, blank=True)
