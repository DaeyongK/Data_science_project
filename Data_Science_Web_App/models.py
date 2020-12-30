from django.db import models

# Create your models here.

class TemporaryFile(models.Model):
    key = models.CharField(max_length = 64)
    data = models.FileField()
