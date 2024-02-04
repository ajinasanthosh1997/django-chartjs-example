# dashboard_app/models.py
from django.db import models

class DataPoint(models.Model):
    label = models.CharField(max_length=255)
    value = models.FloatField()

    def __str__(self):
        return self.label

class DataPoint2(models.Model):
    label = models.CharField(max_length=255)
    value = models.FloatField()

    def __str__(self):
        return self.label

class DataPoint3(models.Model):
    label = models.CharField(max_length=255)
    value = models.FloatField()

    def __str__(self):
        return self.label
