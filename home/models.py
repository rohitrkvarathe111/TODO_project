from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    no = models.IntegerField(primary_key=True, unique=True)
    date = models.CharField(max_length=20)
    task = models.CharField(max_length=200)