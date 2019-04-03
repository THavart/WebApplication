from django.urls import path, include
from django.core.mail import send_mail
from . import views

urlpatterns = [
    path('', views.home, name = 'Homepage'),
]
