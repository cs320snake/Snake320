from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Team(models.Model):
    userOwner = models.ForeignKey(User, on_delete= models.CASCADE)
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    lastname = models.IntegerField(max_length=30);
    score = models.IntegerField();
    