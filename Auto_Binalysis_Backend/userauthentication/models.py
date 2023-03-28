from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class client_detailsManager(BaseUserManager):
    def create_user(self, email, username, org_name, org_city, org_country, account_name, password=None):
        if not email:
            raise ValueError("Email is not provided.")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, org_name=org_name, org_city=org_city, org_country=org_country, account_name=account_name
                          )
        user.set_password(password)
        user.save()

        return user


class client_details(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=100, unique=True, primary_key=True, default='1')
    org_name = models.CharField(max_length=100, null=True)
    org_country = models.CharField(max_length=100, null=True)
    org_city = models.CharField(max_length=100, null=True)
    account_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=100, null=True)
    client_type = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

    objects = client_detailsManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password', 'org_name',
                       'org_city', 'org_country', 'account_name']

    class Meta:
        db_table = 'client_details'


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
