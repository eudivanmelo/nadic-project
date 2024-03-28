from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=16, decimal_places=2)
    
    def __str__(self) -> str:
        return f"{self.name}, {self.user}, {self.account_id}"

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    TYPE_CHOICES = (
        ('Expense', 'Expense'),
        ('Revenue', 'Revenue'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=16, decimal_places=2)
    name = models.CharField(max_length=100)
