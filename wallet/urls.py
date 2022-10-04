from django import views
from django.urls import path
from .views import register_account, register_card, register_currency, register_customer, register_notification, register_reciept, register_reward, register_thirdparty, register_transaction, register_wallet,list_customer 

urlpatterns= [
    path("customer/",register_customer,name="customer"),
    path("currency/",register_currency,name="currency"),
    path("wallet/",register_wallet,name="wallet"),
    path("account/",register_account,name="account"),
    path("thirdparty/",register_thirdparty,name="thirdparty"),
    path("transaction/",register_transaction,name="transaction"),
    path("card/",register_card,name="card"),
    path("notification/",register_notification,name="notification"),
    path("reciept/",register_reciept,name="reciept"),
    path("reward/",register_reward,name="reward"),


    path("customers",list_customer,name="customer_list")

]
   
