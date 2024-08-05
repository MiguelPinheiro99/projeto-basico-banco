from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('criar_conta/', views.criar_conta, name='criar_conta'),
    path('exibir_conta/', views.exibir_conta, name='exibir_conta'),
    path('exibir_tudo/', views.exibir_tudo, name='exibir_tudo'),
    path('deposito/', views.deposito, name='deposito'),
    path('saque/', views.saque, name='saque'),
    path('transferencia/', views.transferencia, name='transferencia'),
]