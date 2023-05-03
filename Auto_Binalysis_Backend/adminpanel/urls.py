from django.urls import path
from . import views


# URL Conf
urlpatterns = [
    path('users/', views.get_users),
    path('delete-user/', views.delete_user),
    path('update-user/', views.update_user)
]
