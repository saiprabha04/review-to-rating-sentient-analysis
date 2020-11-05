from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    User = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)

    def __str__(self):
        return self.User 