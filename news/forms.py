from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from news.models import Business, Neighbourhood


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class NeighbourhoodForm(forms.ModelForm):
	
	class Meta:
		model = Neighbourhood
		fields = ['neighbourhood_name','neighbourhood_location','occupants_count','admin']


class BusinessForm(forms.ModelForm):
	
	class Meta:
		model = Business
		fields = ['business_name','neighbourhood_name','business_email']
