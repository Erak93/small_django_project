# WE ARE GOING TO USER THE FAKER LIBRARY IN ORDER TO POPULATE OUR DATABASE. FIRST WE NEED TO INSTALL IT WITH pip install Faker

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','challenge_project.settings')

import django
django.setup()



#FAKE POP SCRIPT

import random
from app_challenge.models import User
from faker import Faker

fake=Faker()

def populate(N=1):
    for entry in range(N):
        fake_name=fake.name().split() # here we are splitting the fake name generated because we need first and last. Remember that split() creates a list
        fake_first_name=fake_name[0]
        fake_last_name=fake_name[1]
        fake_email_address=fake.email()

        # New entry
        user=User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email_address)[0]# we always need to grab the first tuple index of get or create


if __name__== '__main__':
    print("You are populating your database with dummy data")
    populate(30)
    print("Database populated with new entries")