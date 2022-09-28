

from django.shortcuts import redirect, render
from .models import *
from arp_panel.models import *



def emp_sale_billings(request):
    sale = Sale_Bill.objects.all()
 
    context = {
        'ss':sale,

    }
    return render(request,"emparp_panel/emp_sale_billings.html",context)

def emp_add_sale_invoice(request):
    partys = Party.objects.all()
    fana = Accounting_year.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        party_name = data["party_name"]
        subtotal_amount = data["subtotal_amount"]
        final_amount = data["final_amount"]
        payment_type = data["payment_type"]
        state_of_supply = data["state_of_supply"]
        description = data["description"]
        year = data["year"]

        par = Party.objects.get(name=party_name)
        fan = Accounting_year.objects.get(year=year)

        sb = Sale_Billings(
            date = date,
            party_name = par,
            subtotal_amount = subtotal_amount,
            final_amount = final_amount,
            payment_type = payment_type,
            state_of_supply = state_of_supply,
            description = description,
            year = fan
            )
        sb.save()
        return redirect("emp_sale_billings")
    return render(request,"emparp_panel/emp_add_sale_invoice.html",{'STATE':STATE,"party":partys,"fan":fana})

def emp_edit_sale_invoice(request,id):
    partys = Party.objects.all()
    fana = Accounting_year.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        party_name = data["party_name"]
        subtotal_amount = data["subtotal_amount"]
        final_amount = data["final_amount"]
        payment_type = data["payment_type"]
        state_of_supply = data["state_of_supply"]
        description = data["description"]
        year = data["year"]


        par = Party.objects.get(name=party_name)
        fan = Accounting_year.objects.get(year=year)
        
        s = Sale_Billings.objects.get(pk=id)
        s.date = date
        s.party_name = par
        s.subtotal_amount = subtotal_amount
        s.final_amount = final_amount
        s.payment_type = payment_type
        s.state_of_supply = state_of_supply
        s.description = description
        s.year = fan

        s.save()
        return redirect("emp_sale_billings")
    else:
        sbo = Sale_Billings.objects.get(pk=id)
    return render(request,"emparp_panel/emp_edit_sale_invoice.html",{"STATE":STATE,"party":partys,"fan":fana})

def emp_delete_sale_invoice(request,id):
    dso = Sale_Billings.objects.filter(id=id)
    dso.delete()
    context = {
        'dso':dso,
    }
    return redirect('emp_sale_billings')


def emp_sale_return(request):
    SR = Sale_Return.objects.all()
    context = {
        'sr':SR,
    }
    return render(request,"emparp_panel/emp_sale_return.html",context)

def emp_add_sale_return(request):
    partys = Party.objects.all()
    fana = Accounting_year.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        bill_no = data["bill_no"]
        emp_party_name = data["emp_party_name"]
        total_sale = data["total_sale"]
        balance = data["balance"]
        year = data["year"]

        par = Party.objects.get(name=emp_party_name)
        fan = Accounting_year.objects.get(year=year)


        sr = Emp_Sale_Return(
            date = date,
            emp_party_name = par,
            bill_no = bill_no,
            total_sale = total_sale,
            balance = balance,
            year = fan
            )
        sr.save()
        return redirect("emp_sale_return")
    return render(request,"emparp_panel/emp_add_sale_return.html",{"party": partys,"fan":fana})

def emp_edit_sale_return(request,id):
    partys = Party.objects.all()
    fana = Accounting_year.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        bill_no = data["bill_no"]
        emp_party_name = data["emp_party_name"]
        total_sale = data["total_sale"]
        balance = data["balance"]
        year = data["year"]

        par = Party.objects.get(name=emp_party_name)
        fan = Accounting_year.objects.get(year=year)



        t = Emp_Sale_Return.objects.get(pk=id)
        t.date = date
        t.emp_party_name = par
        t.bill_no = bill_no
        t.total_sale = total_sale
        t.balance = balance
        t.year = fan


        t.save()
        return redirect("emp_sale_return")
    else:
        esr = Emp_Sale_Return.objects.get(pk=id)
    return render(request,"emparp_panel/emp_edit_sale_return.html",{"esr":esr,"party":partys,"fan":fana})

def emp_delete_sale_return(request,id):
    dsr = Emp_Sale_Return.objects.filter(id=id)
    dsr.delete()
    context = {
        'dsr':dsr,
    }
    return redirect('emp_sale_return')


def emp_sale_challan(request):
    SC = Sale_Challan.objects.all()
    context = {
        'sc':SC,
    }
    return render(request,"emparp_panel/emp_sale_challan.html",context)

def emp_add_sale_challan(request):
    partys = Party.objects.all()
    fana = Accounting_year.objects.all()
    emp = Emp.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        challan_no = data["challan_no"]
        party_name = data["party_name"]
        subtotal_amount = data["subtotal_amount"]
        final_amount = data["final_amount"]
        employee_name = data["employee_name"]
        state_of_supply = data["state_of_supply"]
        description = data["description"]
        year = data["year"]

        par = Party.objects.get(name=party_name)
        fan = Accounting_year.objects.get(year=year)
        emp = Emp.objects.get(name=employee_name)


        sc = Sale_Challan(
            date = date,
            challan_no = challan_no,
            party_name = par,
            subtotal_amount = subtotal_amount,
            final_amount = final_amount,
            employee_name = emp,
            state_of_supply = state_of_supply,
            description = description,
            year = fan
            )
        sc.save()
        return redirect("emp_sale_challan")
    return render(request,"emparp_panel/emp_add_sale_challan.html",{"STATE":STATE,"party": partys,"fan":fana,"emp":emp})

def emp_edit_sale_challan(request,id):
    partys = Party.objects.all()
    fana = Accounting_year.objects.all()
    emp = Emp.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        challan_no = data["challan_no"]
        party_name = data["party_name"]
        subtotal_amount = data["subtotal_amount"]
        final_amount = data["final_amount"]
        employee_name = data["employee_name"]
        state_of_supply = data["state_of_supply"]
        description = data["description"]
        year = data["year"]

        par = Party.objects.get(name=party_name)
        fan = Accounting_year.objects.get(year=year)
        emp = Emp.objects.get(name=employee_name)



        t = Sale_Challan.objects.get(pk=id)
        t.date = date
        t.challan_no = challan_no
        t.party_name = par
        t.subtotal_amount = subtotal_amount
        t.final_amount = final_amount
        t.employee_name = emp
        t.state_of_supply = state_of_supply
        t.description = description
        t.year = fan


        t.save()
        return redirect("emp_sale_challan")
    else:
        esc = Sale_Challan.objects.get(pk=id)
    return render(request,"emparp_panel/emp_edit_sale_challan.html",{"STATE":STATE,"esc":esc,"party":partys,"fan":fana,"emp":emp})

def emp_delete_sale_challan(request,id):
    dsc = Sale_Challan.objects.filter(id=id)
    dsc.delete()
    context = {
        'dsc':dsc,
    }
    return redirect('emp_sale_challan')

def emp_add_items(request):
    prods = Product.objects.all()
    servs = Service.objects.all()
    if request.method == "POST":
        data = request.POST
        print(data)
        name = data["name"]
        hsn_code = data["hsn_code"]
        description = data["description"]
        quantity = data["quantity"]
        unit = data["unit"]
        rate = data["rate"]
        average_purchase_price = data["average_purchase_price"]
        max_purchase_price = data["max_purchase_price"]
        subtotal = data["subtotal"]
        date = data["date"]
        # discount = data["discount"]
        tax = data["tax"]
        # prod = Product.objects.get(name= item_name)
        ex = Product(
            name = name,
            hsn_code = hsn_code,
            # discount = discount,
            # description = description,
            # tax = tax,
            # subtotal = subtotal,
            # average_purchase_price = average_purchase_price,
            # max_purchase_price = max_purchase_price,
            # rate = rate,
            unit = unit,
            date = date,
            # quantity = quantity,
            )
        ex.save()
    return render(request,"emparp_panel/emp_add_items.html",{"prd": prods, "ser": servs})


def emp_edit_product(request, id):
    ep = Product.objects.get(pk=id)
    prods = Product.objects.all()
    return render(request, "emparp_panel/emp_add_items.html", {'ep':ep,"prd": prods})

def emp_add_items1(request):
    prods = Product.objects.all()
    servs = Service.objects.all()
    if request.method == "POST":
        data = request.POST
        print(data)
        name = data["name"]
        hsn_code = data["hsn_code"]
        description = data["description"]
        quantity = data["quantity"]
        unit = data["unit"]
        rate = data["rate"]
        average_purchase_price = data["average_purchase_price"]
        max_purchase_price = data["max_purchase_price"]
        subtotal = data["subtotal"]
        date = data["date"]
        # discount = data["discount"]
        tax = data["tax"]
        # prod = Product.objects.get(name= item_name)
        ex = Product(
            name = name,
            hsn_code = hsn_code,
            # discount = discount,
            # description = description,
            # tax = tax,
            # subtotal = subtotal,
            # average_purchase_price = average_purchase_price,
            # max_purchase_price = max_purchase_price,
            # rate = rate,
            unit = unit,
            date = date,
            # quantity = quantity,
            )
        ex.save()
    return render(request,"emparp_panel/emp_add_items1.html",{"prd": prods, "ser": servs})


def emp_edit_product1(request, id):
    ep = Product.objects.get(pk=id)
    prods = Product.objects.all()
    return render(request, "emparp_panel/emp_add_items1.html", {'ep':ep,"prd": prods})



def emp_edit_add_items(request):
    prods = Product.objects.all()
    servs = Service.objects.all()
    if request.method == "POST":
        data = request.POST
        name = data["name"]
        hsn_code = data["hsn_code"]
        description = data["description"]
        quantity = data["quantity"]
        unit = data["unit"]
        rate = data["rate"]
        average_purchase_price = data["average_purchase_price"]
        max_purchase_price = data["max_purchase_price"]
        subtotal = data["subtotal"]
        date = data["date"]
        # discount = data["discount"]
        tax = data["tax"]
        # prod = Product.objects.get(name= item_name)
        ex = Product(
            name = name,
            hsn_code = hsn_code,
            # discount = discount,
            # description = description,
            # tax = tax,
            # subtotal = subtotal,
            # average_purchase_price = average_purchase_price,
            # max_purchase_price = max_purchase_price,
            # rate = rate,
            unit = unit,
            date = date,
            # quantity = quantity,
            )
        ex.save()
    return render(request,"emparp_panel/emp_edit_challan_add_items.html",{"prd": prods, "ser": servs})


def emp_edit_add_product(request, id):
    esc = Product.objects.get(pk=id)
    prods = Product.objects.all()
    return render(request, "emparp_panel/emp_edit_challan_add_items.html", {'esc':esc,"prd": prods})

