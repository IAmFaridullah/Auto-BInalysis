from django.urls import path
from . import views


# URL Conf
urlpatterns = [
    # path('hello/', views.sayhello),
    path('train-model/', views.train_model)
]