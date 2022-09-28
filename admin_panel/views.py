from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"base.html")


# def login(request):
#     return render(request,"login.html")


# def my_profile(request):
#     return render(request,"my_profile.html")


def admin_dash(request):
    return render(request,"admin_dash.html")

def designation(request):
    if request.user.is_staff:
        print("sa"*100)
        designation = Designation.objects.all()
        return render(request,"masters/designation/designation.html",{"designations":designation})
    else:
        messages.warning(request,"Please Login with Admin credentials!!")
        return redirect("login")


def designation_add(request):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            designation = data["designation"]
            if not Designation.objects.filter(name=designation).exists():
                p = Designation(name=designation)
                p.save()
                return redirect("designation")
            else:
                return HttpResponse("designation Already exist")
        return render(request,"masters/designation/designation_add.html")
    else:
        return redirect("login")


def designation_edit(request,id):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            text = data["designation"]
            p = Designation.objects.get(pk=id)
            p.name = text
            p.save()
            return redirect("designation")
        else:
            designation = Designation.objects.get(pk=id)
        return render(request,"masters/designation/designation_edit.html",{"designation":designation})
    else:
        return redirect("login")


def designation_delete(request,id):
    
    if request.user.is_staff:
        des = Designation.objects.get(pk=id)
        des.delete()
        return redirect("designation")
    else:
        return redirect("login")



def place(request):
    
    if request.user.is_staff:
        places = Place.objects.all()
    
        return render(request,"masters/place/place.html",{"places":places})
    else:
        return redirect("login")

def place_add(request):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            place_name = data["placename"]
            # p = Place.objects.get(name=place_name)
            if not Place.objects.filter(name=place_name).exists():
                p = Place(name=place_name)
                p.save()
                return redirect("place")
            else:
                return HttpResponse("place Already exist")
        return render(request,"masters/place/place_add.html")
    else:
        return redirect("login")


def place_edit(request,id):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            place_name = data["placename"]
            place = Place.objects.get(pk=id)
            place.name = place_name
            place.save()
            return redirect("place")
        else:
            place = Place.objects.get(pk=id)
        return render(request,"masters/place/place_edit.html",{"place":place})
    else:
        return redirect("login")


def place_delete(request,id):
    
    if request.user.is_staff:
        des = Place.objects.get(pk=id)
        des.delete()
        return redirect("place")
    else:
        return redirect("login")





def accounting_year(request):
    
    if request.user.is_staff:
        places = Accounting_year.objects.all()
    
        return render(request,"masters/accounting_year/accounting_year.html",{"places":places})
    else:
        return redirect("accounting_year")

def accounting_year_add(request):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            place_name = data["placename"]
            fromdate = data["fromdate"]
            todate = data["todate"]
            # p = Place.objects.get(name=place_name)
            if not Accounting_year.objects.filter(year=place_name).exists():
                p = Accounting_year(year=place_name,
                fromdate = fromdate,
                todate = todate)
                p.save()
                return redirect("accounting_year")
            else:
                return HttpResponse("Accounting year Already exist")
        return render(request,"masters/accounting_year/accounting_year_add.html")
    else:
        return redirect("login")


def accounting_year_edit(request,id):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            place_name = data["placename"]
            fromdate = data["fromdate"]
            todate = data["todate"]
            place = Accounting_year.objects.get(pk=id)
            place.year = place_name
            place.fromdate = fromdate
            place.todate = todate
            place.save()
            return redirect("accounting_year")
        else:
            place = Accounting_year.objects.get(pk=id)
        return render(request,"masters/accounting_year/accounting_year_edit.html",{"place":place})
    else:
        return redirect("login")


def accounting_year_delete(request,id):
    
    if request.user.is_staff:
        des = Accounting_year.objects.get(pk=id)
        des.delete()
        return redirect("accounting_year")
    else:
        return redirect("login")






def holiday(request):
    
    if request.user.is_staff:
        holidays = Holiday.objects.all()
       
        return render(request,"masters/holiday/holiday.html",{"holidays":holidays,})
    else:
        return redirect("login")


def holiday_add(request):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            year = data['accounting_year']
            year = Accounting_year.objects.get(id = year)
            date = data["date"]
            reason = data["reason"]
            if not Holiday.objects.filter(holiday_date=date).exists():

                p = Holiday(reason=reason,holiday_date=date,accounting_year=year)
                p.save()
                return redirect("holiday")
            else:
                return HttpResponse("Holiday date is already present")
        accounting_year = Accounting_year.objects.all()   
        return render(request,"masters/holiday/holiday_add.html",{"accounting_year":accounting_year})
    else:
        return redirect("login")


def holiday_edit(request,id):
    
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            reason = data["reason"]
            date = data["date"]
            holiday = Holiday.objects.get(pk=id)
            holiday.reason = reason
            holiday.holiday_date = date
            holiday.save()
            return redirect("holiday")
        else:
            holiday = Holiday.objects.get(pk=id)
            accounting_year = Accounting_year.objects.all()
        return render(request,"masters/holiday/holiday_edit.html",{"holiday":holiday,"accounting_year":accounting_year})
    else:
        return redirect("login")


def holiday_delete(request,id):
    
    if request.user.is_staff:
        des = Holiday.objects.get(pk=id)
        des.delete()
        return redirect("holiday")
    else:
        return redirect("login")





def arp_items(request):
    
    if request.user.is_staff:
        products = Product.objects.all()
        services = Service.objects.all()
        return render(request,"masters/arp_items/arp_items.html",{"products":products,"services":services})
    else:
        return redirect("login")





def product_add(request):
    
    if request.user.is_staff:
        if request.method == "POST":
        
            data = request.POST
            productname = data["productname"]
            category = data["category"]
            category = Category.objects.get(name = category)
            hsn_code = data["hsn_code"]
            product_code = data["product_code"]
            sale_price = data["sale_price"]
            sale_price_type = data["sale_tax_type"]
            purchase_price = data["purchase_price"]
            purchase_price_type = data["purchase_taxtype"]
            tax_rate = data["tax_rate"]
            
            opening_stock = data["opening_stock"]
            price_per_unit = data["price_per_unit"]
            date = data["date"]
            minimum_stock_quantity = data["minimum_stock_quantity"]
            unit = data["unit"]

            p = Product(
            name = productname,
            category = category,
            hsn_code = hsn_code,
            product_code = product_code,
            sale_price = sale_price,
            sale_price_type = sale_price_type,
            purchase_price = purchase_price,
            purchase_price_type = purchase_price_type,
            tax_rate = tax_rate,
            opening_stock = opening_stock,
            price_per_unit = price_per_unit,
            date = date,
            minimum_stock_quantity = minimum_stock_quantity,
            unit = unit 
            )
            
        
            p.save()
            return redirect("arp_items")
        else:
            product = Product.objects.all()
            categorys = Category.objects.all()
            gst = gstStatic
        return render(request,"masters/arp_items/product_add.html",{"product":product,"categorys":categorys,"gst":gst})
    else:
        return redirect("login")


def product_edit(request,id):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            productname = data["productname"]
            category = data["category"]
            category = Category.objects.get(name = category)
            hsn_code = data["hsn_code"]
            product_code = data["product_code"]
            sale_price = data["sale_price"]
            sale_price_with_tax = data["sale_tax_type"]
            purchase_price = data["purchase_price"]
            purchase_price_with_tax = data["purchase_taxtype"]
            tax_rate = data["tax_rate"]
            
            opening_stock = data["opening_stock"]
            price_per_unit = data["price_per_unit"]
            date = data["date"]
            minimum_stock_quantity = data["minimum_stock_quantity"]
            unit = data["unit"]

            p = Product.objects.get(pk=id)
            p.name = productname
            p.category = category
            p.hsn_code = hsn_code
            p.product_code = product_code
            p.sale_price = sale_price
            p.sale_price_type = sale_price_with_tax
            p.purchase_price = purchase_price
            p.purchase_price_type = purchase_price_with_tax
            p.tax_rate = tax_rate
            p.opening_stock = opening_stock
            p.price_per_unit = price_per_unit
            p.date = date
            p.minimum_stock_quantity = minimum_stock_quantity
            p.unit = unit
            p.save()
            return redirect("arp_items")
        else:
            product = Product.objects.get(pk=id)
            categorys = Category.objects.all()
            gst = gstStatic
            print(product.tax_rate)
        return render(request,"masters/arp_items/product_edit.html",{"product":product,"categorys":categorys,"gst":gst})
    else:
        return redirect("login")


def product_delete(request,id):
    
    if request.user.is_staff:
        des = Product.objects.get(pk=id)
        des.delete()
        return redirect("arp_items")
    else:
        return redirect("login")








def service_add(request):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            sname = data["name"]
            hsn = data["hsn"]
            price = data["price"]
            tax_type = data["tax_type"]
            tax_rate = data["tax_rate"]
            
        
            p = Service(name=sname,hsn_code= hsn,sale_price= price,sale_price_type = tax_type,tax_rate = tax_rate)
        
            p.save()
            return redirect("arp_items")
        else:
            gst = gstStatic
        return render(request,"masters/arp_items/service_add.html",{"service":Service,"gst":gst})
    else:
        return redirect("login")


def service_edit(request,id):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            sname = data["name"]
            hsn = data["hsn"]
            price = data["price"]
            tax_type = data["tax_type"]
            tax_rate = data["tax_rate"]
            
            p = Service.objects.get(pk=id)

            p.name = sname
            p.hsn_code = hsn
            p.sale_price = price
            p.sale_price_type = tax_type
            p.tax_rate = tax_rate
            p.save()
            return redirect("arp_items")
        else:
            service = Service.objects.get(pk=id)
            print(service.name)
            gst = gstStatic
        return render(request,"masters/arp_items/service_edit.html",{"service":service,"gst":gst})
    else:
        return redirect("login")


def service_delete(request,id):
    
    if request.user.is_staff:
        des = Service.objects.get(pk=id)
        des.delete()
        return redirect("arp_items")
    else:
        return redirect("login")







def prp_items(request):
    
    if request.user.is_staff:
        # products = PrpProduct.objects.all()
        services = PrpService.objects.all()
        return render(request,"masters/prp_items/prp_items.html",{"services":services})
    else:
        return redirect("login")





def prp_service_add(request):
   
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            sname = data["name"]
            hsn = data["hsn"]
            service_code = data["service_code"]
            price = data["price"]
            p = PrpService(name=sname,hsn_code= hsn,service_code = service_code,service_price = price)
        
            p.save()
            return redirect("arp_items")
        
        return render(request,"masters/arp_items/prp_service_add.html")
    else:
        return redirect("login")






def arp_party(request):
    
    if request.user.is_staff:
        party = Party.objects.all()
        return render(request,"masters/arp_party/arp_party.html",{"party":party})
    else:
        return redirect("login")


def arp_party_add(request):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            sname = data["name"]
            phone = data["phone"]
            address = data["address"]
            email = data["email"]
            state = data["state"]
            date = data["date"]
            opening_balance = data["opening_balance"]
            gst_number = data["gst_number"]
        
            p = Party(name=sname,phone= phone,address= address,
            email = email,state = state,date=date,opening_balance=opening_balance,gst_number=gst_number)
        
            p.save()
            return redirect("arp_party")
        return render(request,"masters/arp_party/arp_party_add.html")
    else:
        return redirect("login")


def arp_party_edit(request,id):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            sname = data["name"]
            phone = data["phone"]
            address = data["address"]
            email = data["email"]
            state = data["state"]
            date = data["date"]
            opening_balance = data["opening_balance"]
            gst_number = data["gst_number"]
        
            p = Party.objects.get(pk=id)
            p.name = sname
            p.phone = phone
            p.address = address
            p.email = email
            p.state = state
            p.date = date
            p.opening_balance = opening_balance
            p.gst_number = gst_number
            p.save()
            return redirect("arp_party")
        else:
            party = Party.objects.get(pk=id)
        return render(request,"masters/arp_party/arp_party_edit.html",{"party":party})
    else:
        return redirect("login")


def arp_party_delete(request,id):
    
    if request.user.is_staff:
        des = Party.objects.get(pk=id)
        des.delete()
        return redirect("arp_party")
    else:
        return redirect("login")







def prp_party(request):
    
    if request.user.is_staff:
        party = PrpParty.objects.all()
        return render(request,"masters/prp_party/prp_party.html",{"party":party})
    else:
        return redirect("login")


def prp_party_add(request):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            sname = data["name"]
            phone = data["phone"]
            address = data["address"]
            email = data["email"]
            state = data["state"]
            date = data["date"]
            opening_balance = data["opening_balance"]
            gst_number = data["gst_number"]
        
            p = PrpParty(name=sname,phone= phone,address= address,
            email = email,state = state,date=date,opening_balance=opening_balance,gst_number=gst_number)
        
            p.save()
            return redirect("prp_party")
        return render(request,"masters/prp_party/prp_party_add.html")
    else:
        return redirect("login")


def prp_party_edit(request,id):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            sname = data["name"]
            phone = data["phone"]
            address = data["address"]
            email = data["email"]
            state = data["state"]
            date = data["date"]
            opening_balance = data["opening_balance"]
            gst_number = data["gst_number"]
        
            p = PrpParty.objects.get(pk=id)
            p.name = sname
            p.phone = phone
            p.address = address
            p.email = email
            p.state = state
            p.date = date
            p.opening_balance = opening_balance
            p.gst_number = gst_number
            p.save()
            return redirect("prp_party")
        else:
            party = PrpParty.objects.get(pk=id)
        return render(request,"masters/prp_party/prp_party_edit.html",{"party":party})
    else:
        return redirect("login")


def prp_party_delete(request,id):
    
    if request.user.is_staff:
        des = PrpParty.objects.get(pk=id)
        des.delete()
        return redirect("prp_party")
    else:
        return redirect("login")










def bank_list(request):
    
    if request.user.is_staff:
        bank_list = BankAccount.objects.all()
        return render(request,"masters/bank/bank_list.html",{"bank_list":bank_list})
    else:
        return redirect("login")


def bank_add(request):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            name = data['name']
            balance = data['balance']
            date = data['date']
            b = BankAccount(name=name,balance=balance,as_on=date)
            b.save()
            return redirect("bank_list")
        return render(request,"masters/bank/bank_add.html")
    else:
        return redirect("login")


def bank_delete(request,id):
    
    if request.user.is_staff:
        des = BankAccount.objects.get(pk=id)
        des.delete()
        return redirect("Bank_list")
    else:
        return redirect("login")








def item_category(request):
    
    if request.user.is_staff:
        category = Category.objects.all()
    
        return render(request,"masters/item_category/item_category.html",{"category":category})
    else:
        return redirect("login")


def item_category_add(request):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            cname = data['category']
            b = Category(name=cname)
            b.save()
            return redirect("item_category")
        
        return render(request,"masters/item_category/item_category_add.html")
    else:
        return redirect("login")


def item_category_edit(request,id):
    
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            cname = data["category"]
            p = Category.objects.get(pk=id)
            p.name = cname
            p.save()
            return redirect("item_category")
        else:
            category = Category.objects.get(pk=id)
        
        return render(request,"masters/item_category/item_category_edit.html",{"category":category})
    else:
        return redirect("login")


def item_category_delete(request,id):
    
    if request.user.is_staff:
        des = Category.objects.get(pk=id)
        des.delete()
        return redirect("item_category")
    else:
        return redirect("login")









def expense_item(request):
    
    if request.user.is_staff:
        items = ExpenseItem.objects.all()
        return render(request,"masters/expense_item/expense_item.html",{"items":items})
    else:
        return redirect("login")


def expense_item_add(request):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            iname = data['name']
            iprice = data['price']
            b = ExpenseItem(name=iname,price=iprice)
            b.save()
            return redirect("expense_item")
        
        return render(request,"masters/expense_item/expense_item_add.html")
    else:
        return redirect("login")


def expense_item_edit(request,id):
    
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            iname = data['name']
            iprice = data['price']
            p = ExpenseItem.objects.get(pk=id)
            p.name = iname
            p.price = iprice
            p.save()
            return redirect("expense_item")
        else:
            item = ExpenseItem.objects.get(pk=id)
        
        return render(request,"masters/expense_item/expense_item_edit.html",{"item":item})
    else:
        return redirect("login")


def expense_item_delete(request,id):
    
    if request.user.is_staff:
        des = ExpenseItem.objects.get(pk=id)
        des.delete()
        return redirect("expense_item")
    else:
        return redirect("login")









def expense_category(request):
    
    if request.user.is_staff:
        category = ExpenseCategory.objects.all()
    
        return render(request,"masters/expense_category/expense_category.html",{"category":category})
    else:
        return redirect("login")


def expense_category_add(request):
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            cname = data['category']
            etype = data['expense_type']
            b = ExpenseCategory(name=cname,expenseType=etype)
            b.save()
            return redirect("expense_category")
        else:
            category = ExpenseCategory()

        return render(request,"masters/expense_category/expense_category_add.html",{"category":category})
    else:
        return redirect("login")


def expense_category_edit(request,id):
    
    
    if request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            expname = data["category"]
            expense_type = data["expense_type"]
            p = ExpenseCategory.objects.get(pk=id)
            p.reason = expname
            p.expenseType = expense_type
            p.save()
            return redirect("expense_category")
        else:
            category = ExpenseCategory.objects.get(pk=id)
        
        return render(request,"masters/expense_category/expense_category_edit.html",{"category":category})
    else:
        return redirect("login")




def expense_category_delete(request,id):
    
    if request.user.is_staff:
        des = ExpenseCategory.objects.get(pk=id)
        des.delete()
        return redirect("expense_category")
    else:
        return redirect("login")







# def my_customer(request):
#     return render(request,"my_customer.html")


# def add_customer(request):
#     return render(request,"add_customer.html")


# def place_order(request):
#     return render(request,"place_order.html")


# def cancel_order(request):
#     return render(request,"cancel_order.html")


# def view_place_order(request):
#     return render(request,"view_place_order.html")


# def party_details(request):
#     return render(request,"party_details.html")


# def party_ledger(request):
#     return render(request,"party_ledger.html")


# def cylinder_delivery_report(request):
#     return render(request,"cylinder_delivery_report.html")


# def cancel_order_report(request):
#     return render(request,"cancel_order_report.html")


# def add_place_order(request):
#     return render(request,"add_place_order.html")


