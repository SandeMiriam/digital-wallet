from django import forms

from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Transaction, Wallet  


 
class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

class LoanForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields="__all__"

class CurrencyForm(forms.ModelForm):
    class Meta:
        model=Currency
        fields="__all__"

class Walletform(forms.ModelForm):
    class Meta:
        model=Wallet
        fields="__all__"

class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields="__all__"

class ThirdpartyForm(forms.ModelForm):
    class Meta:
        model= Thirdparty
        fields="__all__"

class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields="__all__"

class CardForm(forms.ModelForm):
    class Meta:
        model=Card
        fields="__all__"

class NotificationForm(forms.ModelForm):
    class Meta:
        model=Notification
        fields="__all__"

class RecieptForm(forms.ModelForm):
    class Meta:
        model=Receipt
        fields="__all__"

class RewardForm(forms.ModelForm):
    class Meta:
        model=Reward
        fields="__all__"

