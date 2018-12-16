"""
Definition of models.
"""

from django.db import models

class accountInfo(models.Model):
    student_name = models.CharField(max_length=200)
    student_password = models.CharField(max_length=200)
    teacher_name = models.CharField(max_length=200)
    teacher_password = models.CharField(max_length=200)


# Create your models here.
