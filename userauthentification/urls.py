from django.urls import path
from userauthentification import views

urlpatterns = [
    
    path('profile/update', views.EditProfile, name = "editprofile"),
]
