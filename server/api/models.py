from django.db import models

# Create your models here.
class Process(models.Model):
    uid = models.IntegerField()
    user = models.CharField(max_length=200)
    pid = models.IntegerField()
    cmd = models.TextField(null=False, blank=False)

class Users(models.Model):
    uid = models.IntegerField()
    user = models.CharField(max_length=200)