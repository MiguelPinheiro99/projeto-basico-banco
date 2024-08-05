from django.contrib import admin
from django.urls import path, include
from app_django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('app_django.urls'))
]
