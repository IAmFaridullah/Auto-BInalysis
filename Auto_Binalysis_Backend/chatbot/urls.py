from django.urls import path
from . import views


# URL Conf
urlpatterns = [
    # path('hello/', views.sayhello),
    path('response/', views.chat_responses)
]