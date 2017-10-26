from django.db import models
# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=5)
    email = models.EmailField(max_length=20)
    suggestion = models.CharField(max_length=200)
    date = models.DateTimeField("date published")