from distutils.command.upload import upload
from email.policy import default
from django.db import models
# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=15)
    id_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    image=models.ImageField(default = 'default.jpg', upload_to = 'image_pics')

class Currency(models.Model):
    name=models.CharField(max_length=20)
    country=models.CharField(max_length=40)
    symbol=models.CharField(max_length=15)     

class Wallet(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    amount=models.IntegerField()
    status=models.CharField(max_length=15)
    balance=models.IntegerField()
    pin=models.TextField(max_length=15)
    date=models.DateTimeField()
    currency=models.ForeignKey(Currency, on_delete=models.CASCADE,null=True)
    
class Account(models.Model):
    account_name=models.CharField(max_length=20)
    account_type=models.CharField(max_length=15)
    savings=models.IntegerField() 
    wallet=models.ForeignKey(Wallet, on_delete=models.CASCADE,null=True)
    destination=models.CharField(max_length=35)

class Thirdparty(models.Model):
    fullname=models.CharField(max_length=20)   
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    transaction_cost=models.IntegerField()
    currency=models.ForeignKey("Account", on_delete=models.CASCADE,related_name="Thirdparty_currency")
    isactive=models.BooleanField()
    account=models.ForeignKey("Account", on_delete=models.CASCADE,related_name="Thirdparty_account")
        
    
class Transaction(models.Model):
    date=models.DateTimeField()
    amount=models.PositiveIntegerField()
    transaction_type=models.CharField(max_length=10)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    thirdparty=models.ForeignKey(Thirdparty, on_delete=models.CASCADE,null=True)
    transaction_code=models.CharField(max_length=4)
    charge=models.IntegerField()
    status=models.CharField(max_length=10)
    
    
class Card(models.Model):
    card_number=models.CharField(max_length=16)
    card_name=models.CharField(max_length=20)
    account=models.ForeignKey("Account", on_delete=models.CASCADE,null=True)
    pin_number=models.CharField(max_length=4)
    serial_code=models.PositiveSmallIntegerField()
    expiry_date=models.DateTimeField()
    card_status=models.CharField(max_length=10)
    signature=models.ImageField(null = True)
    

    
class Notification(models.Model):
    date_created=models.DateTimeField()
    isactive=models.BooleanField()
    recipient=models.ForeignKey("Account", on_delete=models.CASCADE,related_name="Notification_recipient")
    message=models.CharField(max_length=100)   
  
    
    
class Receipt(models.Model):
    receipt_date=models.DateTimeField()
    transaction=models.ForeignKey("Transaction", on_delete=models.CASCADE,related_name="Receipt_transaction")
    receipt_file=models.FileField()
    
 
class Loan(models.Model):
    loan_type=models.CharField(max_length=10)
    amount=models.IntegerField()
    wallet=models.ForeignKey(Wallet, on_delete=models.CASCADE,related_name="Loan_wallet")
    date_and_time=models.DateTimeField()
    loan_terms=models.CharField(max_length=10)
    payment_due_date=models.DateTimeField()
    guarantor=models.CharField(max_length=15)
    balance=models.IntegerField()
    duration=models.CharField(max_length=10)
    interest_rates=models.IntegerField()
    status=models.CharField(max_length=10)
    
    
class Reward(models.Model):
    date_of_reward=models.DateTimeField()
    points=models.IntegerField()
    transaction=models.ForeignKey(Transaction, on_delete=models.CASCADE,related_name="Reward_transaction")
    Wallet=models.ForeignKey(Wallet, on_delete=models.CASCADE,related_name="Reward_wallet")
    
 