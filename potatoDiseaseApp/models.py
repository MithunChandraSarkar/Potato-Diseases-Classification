from django.db import models


class PredictionResult(models.Model):
    result = models.CharField(max_length=255)