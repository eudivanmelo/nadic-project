from django import forms
from .models import Account, Transaction, Category

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'balance']
        
class TransctionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'name', 'date', 'value', 'category']
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']