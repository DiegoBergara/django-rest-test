from django.contrib import admin
from .models import  User, Account, Transaction, Currency

# Register your models here.


admin.site.register(User)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Currency)
