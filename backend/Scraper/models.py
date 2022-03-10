from django.db import models

# Create your models here.
class data(models.Model):
    position = models.IntegerField()
    title = models.CharField(max_length=300)
    link = models.CharField(max_length=300)
    displayed_link = models.CharField(max_length=300)
    snippet = models.CharField(max_length=300)