from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        name=
    
    return render(request,'register.html')