

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Admin(models.Model):
    admin_name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=15)
    neighbourhood_location = models.CharField(max_length=15)
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE)

    def __str__(self):
        return self.neighbourhood_name


# class User(models.Model):
#     user_name = models.CharField(max_length=30)
#     neigbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
#     email_address = models.EmailField()


class Business(models.Model):
    business_name = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood_name = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    business_email = models.EmailField()

    def __str__(self):
        return self.business_name