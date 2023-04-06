from django.urls import path
from . import views
from .views import download_file


# URL Conf
urlpatterns = [
    # path('hello/', views.sayhello),
    path('train-model/', views.train_model),
    path('test-model/', views.test_model),
    path('user-models/', views.user_models),
    path('download/<path:file_path>/', download_file, name='download_file'),

    
]