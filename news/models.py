

from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Admin(models.Model):
    admin_name=models.CharField(max_length=30)

    def __str__(self):
        return self.admin_name


class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=15)
    neighbourhood_location = models.CharField(max_length=15)
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE)

    def __str__(self):
        return self.neighbourhood_name

    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()

    @classmethod
    def find_neigborhood(cls,neigborhood):
        searched_hoods = cls.objects.filter(neighbourhood_name__icontains=neigborhood)
        return searched_hoods

    def update_neighborhood(self,neighbourhood_name,neighbourhood_location,occupants_count,admin):
        self.neighbourhood_name=neighbourhood_name
        self.neighbourhood_location=neighbourhood_location
        self.occupants_count=occupants_count
        self.admin=admin

        self.save()

    def update_occupants():
        pass


# class User(models.Model):
#     user_name = models.CharField(max_length=30)
#     neigbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
#     email_address = models.EmailField()


class Business(models.Model):
    business_name = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood_name = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    business_email = models.EmailField()
    business_image = CloudinaryField("businessimage")

    def __str__(self):
        return self.business_name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_busines(cls,business_name):
        business =cls.objects.filter(business_id__icontains= business_name) 
        return business

    def update_business(self,business_name,neighbourhood_name,business_email,business_image):
        self.business_name=business_name
        self.business_image=business_image
        self.business_email=business_email
        self.neighbourhood_name=neighbourhood_name

        self.save()
    
