from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    Name = models.CharField(max_length  = 100)
    Address = models.CharField(max_length  = 100)
    City = models.CharField(max_length  = 100)
    Country = models.CharField(max_length  = 100)
    TelephoneNumber = models.CharField(max_length=10)
    ImagePath = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Description = models.TextField(max_length  = 1000)
    AvgReview = models.IntegerField(null=True,blank=True)    
    def __str__(self):
         return self.Name      

class Review(models.Model):
    Name = models.CharField(max_length=100)
    Reviews = models.CharField(max_length=1000,null=True)
    Rating = models.IntegerField(null=True)
    Hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    def __str__(self):
        return self.Name+"'s  review"

