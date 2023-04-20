## Here is what to do ##

* Add a new model called User
* It should have these fields
** First name
** Last name
** Email

* Make sure to make the migrations!
* Then create a script that will populate your database with fake Users
* Then confirm the populating through the Admin interface
* Remember to change your urls.py files to deal with the changes to the /user extension

![Screenshot from 2023-04-20 11-13-01.png](/home/dci-student/Documents/full stack course/back end/django/django-level2-challenge/Screenshot from 2023-04-20 11-13-01.png)


## Django steps ##

* Create venv (python3 -m venv django_challenge)
* activate (source django_challenge/bin/activate)
* install django and Faker(the last one for populating with dummy data)
* django_admin startproject name .
* create app with python manage.py startapp name
* register app in settings.py
* update the urls with importing views from the app and import include from django.conf.urls
* in urls.py add connect a view for root or homepage and one view for the page users
* create such views under the app_challenge.views (remember to create template with the respective html files and add it to settings)
* create models in models (everytime we update a model we need to migrate,makemigrations and migrate again)
* Register your models in admin
* create superuser (python3 manage.py createsuperuser) 
  * Username (leave blank to use 'dci-student'): Gia
  * Email address: g....@gmail.com
  * Password: 
  * Password (again):*********
  * Superuser created successfully.
* check if the admin is working by going to http://127.0.0.1:8000/admin/
* create module populate_first_app.py in order to generate dummy data with Faker
import the necessary modules (see populate_first_app.py)
  * use a for loop to populate entry
  * use faker to generate dummy attributes
  * create objects with dummy attributes
  * run populate function after if __name__== '__main__':
* modify the users.html by injecting the information we need
* when you are done deactivate virtual environment (deactivate)