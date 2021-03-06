from tkinter import N
from django.test import TestCase
from .models import *

class ProfileTestClass(TestCase):
    def setUp(self):
        self.nancy = Profile(name = 'Nancy', email = 'kathinimuthinzi@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.nancy,Profile))    

    def test_save_method(self):
        self.nancy.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.nancy.save_profile()
        self.nancy.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)   

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.karen = Neighbourhood(neighbourhood_name = 'Karen',Neighbourhood_location = 'Nairobi',occupants_count = 200,admin="Chief")
        self.karen.create_neigbourhood()

        self.new_hood = Neighbourhood(title = 'Test Project', post = 'This is a random test post', profile = self.me)
        self.new_project.save()  

    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()    

    def test_save_method(self):
        self.test_hood.save_project()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) > 0)  

    def test_delete_method(self):
        self.test_hoods.save_hood()
        self.nancy.delete_hood()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) == 0) 

    def test_get_hoods(self):
        hoods = Hood.projects()
        self.assertTrue(len(hoods)>0)

class BusinessTestClass(TestCase):
    def test_save_method(self):
        self.test_business.save()
        test_businesses = Business.objects.all()
        self.assertTrue(len(test_businesses) > 0)

    def test_save_business(self):
        self.assertEqual(len(Business.objects.all()), 1)

    def test_delete_method(self):
        self.assertTrue(len(business) == 0)    

    def tearDown(self):
        Business.objects.all().delete()
