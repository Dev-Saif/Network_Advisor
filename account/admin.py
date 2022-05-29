from django.contrib import admin

# Register your models here.

from .models import Signup, Profile

admin.site.register(Signup)
admin.site.register(Profile)
