from PIL import Image
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.forms import PasswordInput
# code

ROOM_TYPE = (
    ('Hall','Hall'),
    ('Lab','Lab'),
)

# Create your models here.

class Signup(models.Model):
    username = models.CharField(max_length=25,default="name",null=True)
    email = models.EmailField(max_length=254,default="email",null=True)
    password = models.CharField(max_length=25,default="password",null=True) 
    public_ip = models.GenericIPAddressField(protocol='both',unpack_ipv4='enable',null=True,blank=True,default=0.0)
    validity = models.CharField(max_length=10,editable=False)
        
    def __str__(self):        
        return str(self.username)
    
    """def setValidity(self):
        if not self.public_ip == True :
               self.validity = "Designer"            
        else : self.validity = "endUser"       
        return self.validity"""

class Profile(models.Model):
    user = models.OneToOneField(Signup,on_delete=models.CASCADE,null=False)
    userImg = models.ImageField(upload_to="profile/",default="img.png")       
    floorNum = models.IntegerField(default=1,null=True,blank=True)
    deptName = models.CharField(max_length=25,default="myDept",null=True,blank=True)
    roomType = models.CharField(max_length=8,choices=ROOM_TYPE,default="room",null=True,blank=True)
    roomNum = models.IntegerField(default=1,null=True,blank=True)
    public_ip = models.GenericIPAddressField(protocol='both',unpack_ipv4='enable',null=True,blank=True,default=0.0)
    privte_ip = models.GenericIPAddressField(protocol='both',unpack_ipv4='enable',null=True,blank=True,default=0.0)

    """if Signup.validity == "Designer" :
        public_ip = Signup.public_ip
        privte_ip = None
    else : 
        public_ip = None,
        privte_ip.editable = False"""

    def __str__(self):        
        return str(self.user)    

@receiver(post_save, sender=Signup)
def create_profile(sender, instance, created, **kwargs):
	    if created:
		    Profile.objects.create(user=instance)
  
@receiver(post_save, sender=Signup)
def save_profile(sender, instance, **kwargs): 
    instance.profile.save()	

@receiver(post_save, sender=Signup)
def create_user(sender, instance, password, created, **kwargs):
	    if created:
		    User.objects.create(username=instance,password=password)

@receiver(post_save, sender=Signup)
def create_user(sender, instance, created, **kwargs):
	    instance.user.save()	       