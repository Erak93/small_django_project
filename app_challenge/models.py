from django.db import models

# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50,unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}' # this is how the user shows in the user list in admin interface
