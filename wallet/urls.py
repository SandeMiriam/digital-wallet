from django.urls import path
from .views import register_account, register_card, register_currency, register_customer, register_notification, register_reciept, register_reward, register_thirdparty, register_transaction, register_wallet 

urlpatterns= [
    path("customer/",register_customer,name="registration"),
    path("currency/",register_currency,name="registeration"),
    path("wallet/",register_wallet,name="registeration"),
    path("account/",register_account,name="registeration"),
    path("thirdparty/",register_thirdparty,name="registeration"),
    path("transaction/",register_transaction,name="registeration"),
    path("card/",register_card,name="registeration"),
    path("notification/",register_notification,name="registeration"),
    path("reciept/",register_reciept,name="registeration"),
    path("reward/",register_reward,name="registeration"),

]
   
