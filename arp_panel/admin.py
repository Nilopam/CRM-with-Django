from django.contrib import admin
from .models import *

MyModels = [Purchase_Bill,Purchase_Return,Payment_Out,Sale_Bill,Payment_In,Sale_Return,Expense,Sale_Report,Purchase_Report,Daybook,
           Due_List,Stock_Summary_Report,GSTR1,GSTR2,GSTR3B,Add_Items]

admin.site.register(MyModels)

# Register your models here.
