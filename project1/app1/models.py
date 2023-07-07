from django.db import models

# Create your models here.
class Student(models.Model):
    roll=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)