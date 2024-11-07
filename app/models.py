from django.db import models

# Create your models here.
from django.core.validators import *


class Student(models.Model):
    sname=models.CharField(max_length=100,validators=[MinLengthValidator(5)])
    sid=models.IntegerField()
    semail=models.EmailField()

