from django.db import models
from django.db import models

class Category(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    name = models.CharField(max_length=300,blank=True, null=True)
    image = models.ImageField(upload_to='products/')
    price = models.IntegerField( blank=True, null=True)
    statement = models.CharField(max_length=300, blank=True, null=True)
    power = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
class User(models.Model):
    user_id = models.AutoField(primary_key=True,default=None)
    name = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
class Booking(models.Model):
    vehicle_name = models.CharField(max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    pickup_date = models.DateField()
    return_date = models.DateField()
    

    def __str__(self):
        return f"{self.user.name} - {self.vehicle_name}"