from django.db import models

# Create your models here.
class Service(models.Model):
    image = models.ImageField(upload_to ='uploaded-images/service')
    title = models.CharField(max_length=100)
    description = models.TextField()

class Skills(models.Model):
    skills = models.CharField(max_length=80)

class Exp(models.Model):
    exp = models.CharField(max_length=100)

class Projects(models.Model):
    image = models.ImageField(upload_to='uploaded-images/project')
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=250)