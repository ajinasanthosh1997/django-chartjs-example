# dashboard_app/models.py
from django.db import models

class DataPoint(models.Model):
    label = models.CharField(max_length=255)
    value = models.FloatField()

    def __str__(self):
        return self.label
