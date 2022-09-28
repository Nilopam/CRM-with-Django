
from django.db import models
from admin_panel.models import *

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

class Purchase_Bill(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    bill_no = models.IntegerField()
    party_name = models.ForeignKey(Party,on_delete=models.CASCADE)
    subtotal_amount = models.IntegerField()
    final_amount = models.IntegerField()
    payment_type = models.CharField(max_length=30)
    state_of_supply = models.CharField(max_length=200,choices=STATE,default="SELECT")
    description = models.CharField(max_length=200)
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)
    


    def __str__(self):
        return self.party_name.name

   

class Purchase_Return(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    bill_no = models.IntegerField()
    party_name = models.ForeignKey(Party,on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)

    def __str__(self):
        return self.party_name.name


    

class Payment_Out(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    party_name = models.ForeignKey(Party,on_delete=models.CASCADE)
    party_balance = models.IntegerField()
    paid = models.IntegerField()
    balance_due = models.IntegerField()
    payment_type = models.CharField(max_length=30)
    bank_account = models.ForeignKey(BankAccount,on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.party_name.name

    


class Sale_Bill(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    party_name = models.ForeignKey(Party,on_delete=models.CASCADE)
    subtotal_amount = models.IntegerField()
    final_amount = models.IntegerField()
    payment_type = models.CharField(max_length=30)
    state_of_supply = models.CharField(max_length=200,choices=STATE,default="SELECT")
    description = models.CharField(max_length=200)
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)
    
    #product = models.ForeignKey(ArpProduct,on_delete=models.CASCADE)
    #service = models.ForeignKey(ArpService,on_delete=models.CASCADE)

    def __str__(self):
        return self.party_name.name




class Payment_In(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    party_name = models.ForeignKey(Party,on_delete=models.CASCADE)
    party_balance = models.IntegerField()
    opening_balance = models.IntegerField()
    recieved = models.IntegerField()
    balance_due = models.IntegerField()
    payment_type = models.CharField(max_length=30)
    bank_account = models.ForeignKey(BankAccount,on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)

    def __str__(self):
        return self.party_name.name




class Sale_Return(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    bill_no = models.IntegerField()
    party_name = models.ForeignKey(Party,on_delete=models.CASCADE)
    total_sale = models.IntegerField()
    balance = models.IntegerField()
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.party_name.name



class Expense(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    expense_category = models.CharField(max_length=200)
    total_amount = models.IntegerField()
    payment_type = models.CharField(max_length=30)
    bank_account = models.ForeignKey(BankAccount,on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)

    def __str__(self):
        return self.expense_category





class Sale_Report(models.Model):
    date = models.DateField()
    invoice_no = models.IntegerField()
    bill_type = models.CharField(max_length=200)
    party_name = models.ForeignKey(Party,on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=300)
    total_amount= models.IntegerField()
    recieved_amount = models.IntegerField()
    balance = models.IntegerField()
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)

    def __str__(self):
        return self.party_name.name

class Purchase_Report(models.Model):
    date = models.DateField()
    purchase_bill_no = models.IntegerField()
    bill_type = models.CharField(max_length=200)
    party_name = models.ForeignKey(Party,on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=300)
    total_amount= models.IntegerField()
    recieved_amount = models.IntegerField()
    balance = models.IntegerField()
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)

    def __str__(self):
        return self.party_name.name
    

class Daybook(models.Model):
    date = models.DateField()
    invoice_no = models.IntegerField()
    bill_type = models.CharField(max_length=200)
    particulars = models.CharField(max_length=200)
    debit= models.IntegerField()
    credit = models.IntegerField()
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.invoice_no

class Due_List(models.Model):
    date = models.DateField()
    invoice_no = models.IntegerField()
    bill_type = models.CharField(max_length=200)
    party_name = models.ForeignKey(Party,on_delete=models.CASCADE)
    contact_details = models.IntegerField()
    payment_status = models.CharField(max_length=300)
    total_amount= models.IntegerField()
    recieved_amount = models.IntegerField()
    balance_amaount = models.IntegerField()
    employee_name = models.CharField(max_length=200)
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)

    def __str__(self):
        return self.party_name.name


class Stock_Summary_Report(models.Model):
    date = models.DateField()
    item_name = models.ForeignKey(Product,on_delete=models.CASCADE)
    sale_price = models.IntegerField()
    purchase_price = models.IntegerField()
    stock_qty = models.IntegerField()
    stock_value = models.IntegerField()
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name



class GSTR1(models.Model):
    date = models.DateField()
    hsn = models.IntegerField()
    description = models.CharField(max_length=300)
    uqc = models.CharField(max_length=300)
    taxable_value = models.IntegerField()
    integrated_tax_amount = models.IntegerField()
    central_tax_amount= models.IntegerField()
    state_ui_tax_amount= models.IntegerField()
    cess_amount= models.IntegerField()
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)

    def __str__(self):
        return self.hsn

class GSTR2(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()

class GSTR3B(models.Model):
    date = models.DateField()
    inter_state_supplies = models.CharField(max_length=200)
    intra_state_supplies = models.CharField(max_length=200)
    year = models.ForeignKey(Accounting_year,on_delete=models.CASCADE)

    def __str__(self):
        return self.date



class Add_Items(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)


