from os import name
from django import urls
from django.urls import path
from accounts.views import signin_view

urlpatterns = [
    path('', signin_view, name='index')
]