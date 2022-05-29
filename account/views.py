from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from .models import Signup, Profile 
# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password') 
        public_ip = request.POST.get('public_ip')

        data = Signup(username=username,email=email,password=password,public_ip=public_ip) 
        data.save()
        return render(request,'../../home/templates/requests.html')         
    return render(request,'registration/signup.html')      

def login(request,id):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password') 
        
        data = login(email=email,password=password)
        data.save()
        profile = Profile.objects.get(id=id)
        context = {'profile':profile}  
        return render(request,'Profile/profile.html',context)
    return render(request,'Profile/profile.html')    

def profile(request,id):   
    #profile = Profile.objects.all()
    profile = Profile.objects.get(id=id)
    context = {'profile':profile}    
    return render(request,'Profile/profile.html',context)    

def editProfile():
        pass