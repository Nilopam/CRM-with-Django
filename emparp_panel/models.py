from django.db import models
from admin_panel.models import *
from employee.models import *


STATE = (
    ('SELECT', 'Select'),
    ('ANDHRA PRADESH', 'Andhra Pradesh'),
    ('ASSAM', 'Assam'),
    ('BIHAR', 'Bihar'),
    ('CHHATTISGARH', 'Chhattisgarh'),
    ('GOA', 'Goa'),
    ('GUJRAT', 'Gujrat'),
    ('HARYANA', 'Haryana'),
    ('HIMACHAL PRADESH', 'Himachal Pradesh'),
    ('JHARKHAND', 'Jharkhand'),
    ('KARNATAKA', 'Karnataka'),
    ('KERALA', 'Kerala'),
    ('MADHYA PRADESH', 'Madhya Pradesh'),
    ('MAHARASHTRA', 'Maharashtra'),
    ('MANIPUR', 'Manipur'),
    ('MEGHALAYA', 'Meghalaya'),
    ('MIZORAM', 'Mizoram'),
    ('NAGALAND', 'Nagaland'),
    ('ODISHA', 'Odisha'),
    ('PUNJAB', 'Punjab'),
    ('RAJASTHAN', 'Rajasthan'),
    ('SIKKIM', 'Sikkim'),
    ('TAMILNADU', 'Tamilnadu'),
    ('TELENGANA', 'Telengana'),
    ('TRIPURA', 'Tripura'),
    ('UTTARAKHAND', 'Uttarakhand'),
    ('UTTAR PRADESH', 'Uttar pradesh'),
    ('WEST BENGAL', 'West bengal'),
    ('ANADAMAN & NICOBAR ISLANDS', 'Andaman & Nicobar Islands'),
    ('DADRA and NAGAR HAVELI and DAMAN & DIU', 'Dadra & Nagar Haveli and Daman & Diu'),
    ('JAMMU & KASHMIR', 'Jammu & Kashmir'),
    ('LAKSHADWEEP', 'Lakshadweep'),
    ('THE GOVERNMENT of NCT of DELHI', 'The Government of NCT of Delhi'),
    ('LADAKH', 'Ladakh'),
    ('PUDUCHERRY', 'Puducherry'),


)


class Sale_Billings(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    party_name = models.ForeignKey(Party,on_delete=models.CASCADE)
    subtotal_amount = models.IntegerField()
    final_amount = models.IntegerField()
    payment_type = models.CharField(max_length=30)
    state_of_supply = models.CharField(max_length=200,choices=STATE,default="SELECT")
    description = models.CharField(max_length=200)
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)

    def __str__(self):
        return self.party_name.name

class Emp_Sale_Return(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    bill_no = models.IntegerField()
    emp_party_name = models.ForeignKey(Party,on_delete=models.CASCADE)
    total_sale = models.IntegerField()
    balance = models.IntegerField()
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.emp_party_name.name


class Sale_Challan(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    challan_no = models.IntegerField()
    party_name = models.ForeignKey(Party,on_delete=models.CASCADE)
    subtotal_amount = models.IntegerField()
    final_amount = models.IntegerField()
    employee_name = models.ForeignKey(Emp,on_delete=models.CASCADE)
    state_of_supply = models.CharField(max_length=200,choices=STATE,default="SELECT")
    description = models.CharField(max_length=200)
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.party_name.name

class Emp_Add_Items(models.Model):
    emp_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    emp_service = models.ForeignKey(Service,on_delete=models.CASCADE)






