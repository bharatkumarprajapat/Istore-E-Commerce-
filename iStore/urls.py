# urls.py (in your main project)

from django.urls import path

from . import views
from .views import register, user_login

urlpatterns = [
    path('', views.Home, name='Home'),
    path('register/', register, name='register'),
    path('user_login/', user_login, name='login'),
    # Other URL patterns for your project...
]
