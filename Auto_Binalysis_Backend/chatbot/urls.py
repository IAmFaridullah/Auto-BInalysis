from django.urls import path
from . import views


# URL Conf
urlpatterns = [
    # path('hello/', views.sayhello),
    path('response/', views.chat_response),
    path('upload/', views.dataset_upload),
    path('chats/', views.get_chats),
    path('user-chats/', views.get_user_chats),
    path('admin-chat/', views.admin_message)
]
