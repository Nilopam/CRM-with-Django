from django.db import models

# Create your models here.

class Designation(models.Model):

    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class Place(models.Model):

    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class Accounting_year(models.Model):

    
    year = models.CharField( max_length=50,unique=True)
    fromdate = models.DateField(auto_now=False, auto_now_add=False,unique=True)
    todate = models.DateField(auto_now=False, auto_now_add=False,unique=True)
    

    def __str__(self):
        return self.year

    

class Holiday(models.Model):

    accounting_year = models.ForeignKey("Accounting_year", on_delete=models.CASCADE)
    holiday_date = models.DateField(auto_now=False, auto_now_add=False,unique=True)
    on_account_of = models.CharField(max_length=100)

    def __str__(self):
        return self.accounting_year


class Category(models.Model):

    name = models.CharField( max_length=100,unique=True)

    def __str__(self):
        return self.name


# class Gst(models.Model):

#     name = models.CharField( max_length=50)
#     tax_value = models.DecimalField( max_digits=5, decimal_places=2)

#     def __str__(self):
#         return self.name

gstStatic = (
    ('0.25','GST@0.25%'),
    ('0.25','IGST@0.25%'),
    ('3.0','GST@3%'),
    ('3.0','IGST@3%'),
    ('5.0','GST@5%'),
    ('5.0','IGST@5%'),
    ('12.0','GST@12%'),
    ('18.0','GST@18%'),
    ('18.0','IGST@18%'),
    ('28.0','GST@28%'),
    ('28.0','IGST@28%'),
    ('12.0','IGST@12%'),
    ('0.0','IGST@0%'),
)


class Product(models.Model):

    taxTypes = (
        ('withTax','with Tax'),
        ('withoutTax','without Tax'),
    )

    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)
    hsn_code = models.IntegerField()
    product_code = models.CharField(max_length=100)
    sale_price = models.CharField(max_length=100)
    sale_price_type = models.CharField(choices=taxTypes ,max_length=50)
    purchase_price = models.CharField(max_length=100)
    purchase_price_type = models.CharField(choices=taxTypes ,max_length=50)
    tax_rate = models.CharField(choices=gstStatic,max_length=20)
    opening_stock = models.CharField(max_length=100)
    price_per_unit = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    minimum_stock_quantity = models.IntegerField()
    unit = models.IntegerField()

    def __str__(self):
        return self.name


class Service(models.Model):
    taxTypes = (
            ('withTax','with Tax'),
            ('withoutTax','without Tax'),
        )
    name = models.CharField(max_length=100)
    hsn_code = models.CharField(max_length=100)
    sale_price = models.CharField(max_length=100)
    sale_price_type = models.CharField( choices=taxTypes,max_length=50)
    tax_rate = models.CharField(choices=gstStatic,max_length=20)

    def __str__(self):
        return self.name





class PrpService(models.Model):

    name = models.CharField(max_length=100)
    hsn_code = models.CharField(max_length=100)
    service_code = models.CharField( max_length=50)
    service_price = models.IntegerField()
    
    def __str__(self):
        return self.name



class Party(models.Model):

    name = models.CharField( max_length=100)
    phone = models.CharField( max_length=100)
    address = models.CharField( max_length=100)
    email = models.EmailField( max_length=254)
    state = models.CharField( max_length=100)
    date = models.DateField( auto_now=False, auto_now_add=False)
    opening_balance = models.CharField( max_length=100)
    gst_number = models.CharField( max_length=100)

    def __str__(self):
        return self.name

    
class PrpParty(models.Model):

    name = models.CharField( max_length=100)
    phone = models.CharField( max_length=100)
    address = models.CharField( max_length=100)
    email = models.EmailField( max_length=254)
    state = models.CharField( max_length=100)
    date = models.DateField( auto_now=False, auto_now_add=False)
    opening_balance = models.CharField( max_length=100)
    gst_number = models.CharField( max_length=100)
    
    def __str__(self):
        return self.name


class BankAccount(models.Model):

    name = models.CharField( max_length=100)
    balance = models.CharField( max_length=100)
    as_on = models.DateField( auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.name

    
class ExpenseItem(models.Model):

    name = models.CharField( max_length=100,unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class ExpenseCategory(models.Model):

    expenseTypes = (
        ('indirectExpense','indirect Expense'),
        ('directExpense','direct Expense'),
    )

    name = models.CharField( max_length=100,unique=True)
    expenseType = models.CharField(choices=expenseTypes,max_length=50)

    def __str__(self):
        return self.name
