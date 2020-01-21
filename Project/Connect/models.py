from django.db import models

# Create your models here.
class Teacher(models.Model):
    code = models.CharField(max_length=10)
    location = models.CharField(max_length=40)


class Student(models.Model):
    code = models.CharField(max_length=10)
    location = models.CharField(max_length=40)
