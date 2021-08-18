from os import name
from django import urls
from django.urls import path
from accounts.views import signin_view, signup_view

urlpatterns = [
    path('signin/', signin_view, name='signin'),
    path('signup/', signup_view, name='signup'),
]