from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, age, password=None):
        if not email:
            raise ValueError("Email is not provided.")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, age=age)
        user.set_password(password)
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'age']


# from django.db import models

# # Create your models here.


# class client_details(models.Model):
#     Username = models.CharField(max_length=100, unique=True, primary_key=True)
#     Org_Name = models.CharField(max_length=100)
#     Org_Country = models.CharField(max_length=100)
#     Org_City = models.CharField(max_length=100)
#     Account_Name = models.CharField(max_length=100)
#     Email = models.EmailField(unique=True)
#     Pswd_Hash = models.CharField(max_length=100)
#     Client_Gender = models.CharField(max_length=100)
#     Client_Type = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'client_details'


# class clients_login(models.Model):
#     Username = models.CharField(max_length=100, unique=True, primary_key=True)
#     Password = models.CharField(max_length=100)
#     Pswd_Hash = models.CharField(max_length=100)
#     Client_Type = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'clients_login'
