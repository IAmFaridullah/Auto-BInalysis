from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import clients

class ClientsBackend(BaseBackend):
    def authenticate(self, request, Username=None, password=None, **kwargs):
        try:
            'SELECT * FROM clients_login'
            user = clients.objects.get(Username=Username)
            if user.check_password(password):
                return user
        except clients.DoesNotExist:
            return None

    def get_user(self, Username):
        try:
            return clients.objects.get(pk=Username)
        except clients.DoesNotExist:
            return None