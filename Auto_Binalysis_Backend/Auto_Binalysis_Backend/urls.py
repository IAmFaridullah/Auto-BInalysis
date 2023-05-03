from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('chatbot.urls')),
    path('', include('userauthentication.urls')),
    path('analysis/', include('analysis.urls')),
    path('adminpanel/', include('adminpanel.urls'))

]
