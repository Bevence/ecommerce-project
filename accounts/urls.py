from os import name
from django import urls
from django.urls import path
from accounts.views import signin_view, signup_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signin/', signin_view, name='signin'),
    path('signup/', signup_view, name='signup'),
    path('signout/', LogoutView.as_view(template_name='account/signout.html'), name='logout'),
]
