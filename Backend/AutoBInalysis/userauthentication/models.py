from django.db import models

# Create your models here.
class client_details(models.Model):
    Username = models.CharField(max_length=100, unique=True, primary_key=True)
    Org_Name = models.CharField(max_length = 100)
    Org_Country = models.CharField(max_length = 100)
    Org_City = models.CharField(max_length=100)
    Account_Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Pswd_Hash = models.CharField(max_length = 100)
    Client_Gender = models.CharField(max_length=100)
    Client_Type = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'client_details'

class clients_login(models.Model):
    Username = models.CharField(max_length=100, unique=True, primary_key=True)
    Password = models.CharField(max_length = 100)
    Pswd_Hash = models.CharField(max_length = 100)
    Client_Type = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'clients_login'