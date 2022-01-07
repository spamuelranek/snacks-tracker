from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey
from django.forms.fields import CharField
from django.contrib.auth import get_user_model

# Create your models here.

class Snack(models.Model):
  name = models.CharField(max_length=64, default="")
  purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
  description = models.TextField(max_length=256, default="")

  def __str__(self):
    return self.name