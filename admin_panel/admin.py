from django.contrib import admin
from .models import *
# Register your models here.

myModels = [Designation,Place,Holiday,Category,BankAccount,Party,PrpParty,
ExpenseItem,ExpenseCategory,Product,Service,PrpService,Accounting_year]
admin.site.register(myModels)