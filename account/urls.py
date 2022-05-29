from django.urls import path
from . import views
            
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('profile/',views.login,name='login'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('profile/edit',views.profile,name='profile_edit'),
]