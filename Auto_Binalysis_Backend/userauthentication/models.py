from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class client_detailsManager(BaseUserManager):
    def create_user(self, email, username, client_type, gender, org_name, org_city, org_country, account_name, password=None):
        if not email:
            raise ValueError("Email is not provided.")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, client_type=client_type, gender=gender, org_name=org_name, org_city=org_city, org_country=org_country, account_name=account_name
                          )
        user.set_password(password)
        user.save()

        return user


class client_details(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=100, primary_key=True)
    org_name = models.CharField(max_length=100, null=True, default=None)
    org_country = models.CharField(max_length=100, null=True, default=None)
    org_city = models.CharField(max_length=100, null=True, default=None)
    account_name = models.CharField(max_length=100, null=True, default=None)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=100, null=True, default=None)
    client_type = models.CharField(max_length=100, null=True, default=None)
    gender = models.CharField(max_length=100, null=True, default=None)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = client_detailsManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'client_type', 'gender', 'org_name',
                       'org_city', 'org_country', 'account_name', 'is_admin']

    class Meta:
        db_table = 'client_details'
