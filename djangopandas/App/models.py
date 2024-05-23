from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    age = models.IntegerField()