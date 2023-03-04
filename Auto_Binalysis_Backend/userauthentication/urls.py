from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    # path('login/', views.Login_Page, name="Login_Page"),
    # path('sign-up/', views.SignUp_Page, name="SignUp_Page"),
    # path('sign-up/SignUp_success', views.SignUp_success, name="SignUp_success"),
    # path('sign-up/User_Dashboard', views.User_Dashboard, name="User_Dashboard"),
    # path('login/User_Dashboard', views.User_Dashboard, name="User_Dashboard")
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]
