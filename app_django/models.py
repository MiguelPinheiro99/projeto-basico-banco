from django.db import models

class Conta(models.Model):
    MOEDA_CHOICES = [
        ('real', 'Real'),
        ('dolar', 'Dólar'),
        ('euro', 'Euro'),
    ]

    nome_titular = models.CharField(max_length=20, unique=True)
    numero_conta = models.CharField(max_length=5, unique=True)
    moeda = models.CharField(max_length=10, choices=MOEDA_CHOICES)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nome_titular} ({self.numero_conta})'
