from django.contrib import admin

# Register your models here.
from.models import Account, Card, Customer, Notification, Reward,Currency,Loan,Receipt, Thirdparty, Transaction, Wallet
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name",)
    search_fields=("first_name","last_name",)
admin.site.register(Customer,CustomerAdmin)

admin.site.register(Reward)
admin.site.register(Currency)
admin.site.register(Loan)
admin.site.register(Receipt)
admin.site.register(Notification)
admin.site.register(Card)
admin.site.register(Thirdparty)
admin.site.register(Transaction)
admin.site.register(Account)
admin.site.register(Wallet)

