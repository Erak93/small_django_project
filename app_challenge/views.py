from django.shortcuts import render
from app_challenge.models import User

# Create your views here.

def home(request):
    home_message={'welcome_message':'Go to users to see a list of users'}
    return render (request,'app_challenge/home.html',context=home_message)

def users(request):
    user_list=User.objects.order_by('first_name')
    user_dict={'users':user_list}

    return render (request,'app_challenge/users.html',context=user_dict)
