from django.db import models

class Customer(models.Model):
    user_id = models.BigIntegerField(unique=True)  # ID из Telegram
    phone = models.CharField(max_length=20, blank=True, null=True)
    balance = models.IntegerField(default=0)  # Бонусы
    registration_date = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    points = models.IntegerField()  # + или - бонусы
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
