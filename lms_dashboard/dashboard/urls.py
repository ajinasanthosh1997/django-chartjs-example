# dashboard_project/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import dashboard, get_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('get_data/', get_data, name='get_data'),
]
