from django.db import models

# Create your models here.


class Admin(models.Model):
    Username = models.CharField(max_length=100, primary_key=True)
    Password = models.CharField(max_length=100)
    Admin_Name = models.CharField(max_length=100)
    Admin_Gender = models.CharField(max_length=6, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
    ])

    class Meta:
        db_table = 'admins'
