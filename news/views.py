from multiprocessing import context
from django.shortcuts import  render, redirect
from .forms import *
import datetime as dt
from django.contrib.auth import login, authenticate ,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here.
def home(request):
	
	date = dt.date.today()
	business = Business.objects.all()
	neighbourhood = Neighbourhood.objects.all()
	
	context={
		'date':date,
		'business':business,
		'hoods':neighbourhood,
	}
	return render(request,'home.html',context)

def add_hood(request):

	form = NeighbourhoodForm()
	context = {'form':form}
	if request.method == 'POST':
		form=NeighbourhoodForm(request.POST)
		if form.is_valid():
			hoods = form.save(commit=False)
			hoods.save()
			return redirect('home')

		else:
			form = NeighbourhoodForm()

	return render(request,'add_hood.html',context)

def add_business(request):
	form = BusinessForm()
	context = {
		'form':form,
	}
	# current_user = request.user

	if request.method == "POST":
		form = BusinessForm(request.POST,request.FILES)
		print(request.POST.get('business_image'))
		if form.is_valid():
			business = form.save(commit=False)
			business.user = request.user
			business.save()
			messages.success(request, "Business saved!." )
			return redirect('home')
		else:
			messages.error(request, "Please check your inputs!." )
			form = BusinessForm()

	return render(request,'addbusiness.html',context)

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):

    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("login")