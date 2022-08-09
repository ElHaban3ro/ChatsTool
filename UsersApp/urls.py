from django.contrib import admin
from django.urls import path, include
from .views import user

urlpatterns = [
    path('test/', user, name = 'user_page'),
]
