# authentication/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import CustomLoginView, LogoutView

app_name = 'authentication'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
