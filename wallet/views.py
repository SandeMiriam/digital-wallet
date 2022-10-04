from urllib import request
from django .shortcuts import redirect, render

from wallet.models import Customer

from .forms import AccountForm, CardForm, CurrencyForm, CustomerRegistrationForm, NotificationForm, RecieptForm, RewardForm, ThirdpartyForm, TransactionForm, Walletform

# Create your views here.
def register_customer(request):
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})

def list_customer(request):
    customer=Customer.objects.all()
    return render(request,"wallet/customer_list.html",{"customer":customer})
    
def register_currency(request):
    form=CurrencyForm()
    return render (request,"wallet/register_currency.html",{'form':form})

def register_wallet(request):
    form=Walletform()
    return render (request,"wallet/register_wallet.html",{'form':form})

def register_account(request):
    form=AccountForm()
    return render (request,"wallet/register_account.html",{'form':form})

def register_thirdparty(request):
    form=ThirdpartyForm()
    return render (request,"wallet/register_thirdparty.html",{'form':form})

def register_transaction(request):
    form=TransactionForm()
    return render (request,"wallet/register_transaction.html",{'form':form})

def register_card(request):
    form=CardForm()
    return render (request,"wallet/register_card.html",{'form':form})

def register_notification(request):
    form=NotificationForm()
    return render (request,"wallet/register_notification.html",{'form':form})

def register_reciept(request):
    form=RecieptForm()
    return render (request,"wallet/register_reciept.html",{'form':form})

def register_reward(request):
    form=RewardForm()
    return render (request,"wallet/register_reward.html",{'form':form})

