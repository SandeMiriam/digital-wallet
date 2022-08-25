from django.contrib import admin

# Model registeration
from.models import Account, Card, Customer, Notification, Reward,Currency,Loan,Receipt, Thirdparty, Transaction, Wallet
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","gender",)
    search_fields=("first_name","last_name","gender",)
admin.site.register(Customer,CustomerAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=("transaction","date_of_reward","points",)
    search_fields=("transaction","date_of_reward","points",)
admin.site.register(Reward,RewardAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_type","amount","balance",)
    search_fields=("loan_type","amount","balance",)
admin.site.register(Loan,LoanAdmin)

class RecieptAdmin(admin.ModelAdmin):
    list_display=("receipt_date","transaction",)
    search_fields=("receipt_date","transaction",)
admin.site.register(Receipt,RecieptAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=("date_created","recipient","message",)
    search_fields=("date_created","recipient","message",)
admin.site.register(Notification,NotificationAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=("card_number","card_name","pin_number",)
    search_fields=("card_number","card_name","pin_number",)
admin.site.register(Card,CardAdmin)

class ThirdpartyAdmin(admin.ModelAdmin):
    list_display=("fullname","email","phone_number",)
    search_fields=("fullname","email","phone_number",)
admin.site.register(Thirdparty,ThirdpartyAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=("account_name","account_type","savings",)
    search_fields=("account_name","account_type","savings",)
admin.site.register(Account,AccountAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=("customer","amount","status",)
    search_fields=("customer","amount","status",)
admin.site.register(Wallet,WalletAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display=("name","country","symbol")
    search_fields=("name","country")
admin.site.register(Currency,CurrencyAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("date","amount","customer",)
    search_fields=("date","amount","customer",)
admin.site.register(Transaction,TransactionAdmin)

# admin.site.register(Wallet,WalletAdmin)
# admin.site.register(Account,AccountAdmin)
# admin.site.register(Transaction,TransactionAdmin)
# admin.site.register(Card,CardAdmin,)
# admin.site.register(Thirdparty,ThirdpartyAdmin,)
# admin.site.register(Notification,NotificationAdmin,)
# admin.site.register(Loan,LoanAdmin)
# admin.site.register(Reward,RewardAdmin,)
# admin.site.register(Currency,CurrencyAdmin,)
# admin.site.register(Receipt,RecieptAdmin)