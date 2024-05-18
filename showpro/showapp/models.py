from django.db import models

# Create your models here.
class moviedetails(models.Model):
    moviename=models.CharField(max_length=200)
    rating=models.CharField(max_length=150)
    appearence=models.CharField(max_length=50)
    language=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    genre=models.CharField(max_length=150)
    certification=models.CharField(max_length=50)
    releasedate=models.CharField(max_length=50)
    poster=models.ImageField()
    banner=models.ImageField()



class bmsuser(models.Model):  
    email=models.CharField(max_length=100)
    age=models.IntegerField()
    password=models.CharField(max_length=100)
