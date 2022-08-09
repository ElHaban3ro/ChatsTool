from django.contrib import admin
from django.urls import path, include

from .views import home, SignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),


    path('user/', include('django.contrib.auth.urls')),
    path('user/register/', SignUp.as_view(), name = 'register'),
]
