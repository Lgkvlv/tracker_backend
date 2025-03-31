from django.db import models

class Category(models.Model):
    user_id = models.BigIntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user_id = models.BigIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category}: {self.amount} ₽"
