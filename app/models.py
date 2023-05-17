from django.db import models

# Create your models here.
from django.core import validators
class School(models.Model):
    sname=models.CharField(max_length=100)
    sid=models.IntegerField(primary_key=True,validators=[validators.MaxValueValidator(999)])
    addres=models.TextField()