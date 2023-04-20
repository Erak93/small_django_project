from django.contrib import admin
from django.urls import path
from app_challenge import views


urlpatterns = [
  
    path("",views.users,name='users'),
    
]
