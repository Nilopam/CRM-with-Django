from django.contrib import admin
from .models import *

MyModels = [Sale_Billings,Sale_Challan,Emp_Sale_Return,Emp_Add_Items]

admin.site.register(MyModels)

