from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Match:
    user = models.ForeignKey(User, on_delete=models.CASCADE);
    date = models.DateField();
    score = models.IntegerField();