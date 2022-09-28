from datetime import date

from django.http import HttpResponse
from django.shortcuts import redirect, render

from emparp_panel.models import Sale_Challan
from .models import *
import csv




def purchase_bill(request):
    PB = Purchase_Bill.objects.all()
    context = {
        'pb':PB,
    }
    return render(request,"arp_panel/purchase_bill.html",context)

def add_purchase(request):
    
    partys = Party.objects.all()
    fina = Accounting_year.objects.all()

    
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        bill_no = data["bill_no"]
        party_name = data["party_name"]
        subtotal_amount = data["subtotal_amount"]
        final_amount = data["final_amount"]
        payment_type = data["payment_type"]
        state_of_supply = data["state_of_supply"]
        description = data["description"]
        year = data["year"]
        

        par = Party.objects.get(name=party_name)
        fan = Accounting_year.objects.get(year=year)
        print(par)



        
        
        pb = Purchase_Bill(
            date = date,
            bill_no = bill_no,

            party_name = par,
            subtotal_amount = subtotal_amount,
            final_amount = final_amount,
            payment_type = payment_type,
            state_of_supply = state_of_supply,
            description = description,
            year = fan,
            
        )


        pb.save()
    return render(request,"arp_panel/add_purchase.html",{'STATE':STATE,"party":partys,"fan":fina})

def edit_purchase(request,id):
    partys = Party.objects.all()
    fina = Accounting_year.objects.all()

    if request.method == "POST":
        data = request.POST
        date = data["date"]
        bill_no = data["bill_no"]
        party_name = data["party_name"]
        subtotal_amount = data["subtotal_amount"]
        final_amount = data["final_amount"]
        payment_type = data["payment_type"]
        state_of_supply = data["state_of_supply"]
        description = data["description"]
        year = data["year"]
        

        par = Party.objects.get(name=party_name)
        fan = Accounting_year.objects.get(year=year)



        
        p = Purchase_Bill.objects.get(pk=id)
        p.date = date
        p.bill_no = bill_no
        p.party_name = par
        p.subtotal_amount = subtotal_amount
        p.final_amount = final_amount
        p.payment_type = payment_type
        p.state_of_supply = state_of_supply
        p.description = description
        p.year = fan
        

        p.save()
        return redirect("purchase_bill")
    else:
        ep = Purchase_Bill.objects.get(pk=id)
    return render(request,"arp_panel/edit_purchase.html",{"STATE":STATE,"party":partys,"fan":fina,"ep":ep})

def delete_purchase(request,id):
    dp = Purchase_Bill.objects.filter(id=id)
    dp.delete()
    context = {
        'dp':dp,
    }
    return redirect('purchase_bill')


def purchase_return(request):
    PR = Purchase_Return.objects.all()
    context = {
        'pr':PR,
    }
    return render(request,"arp_panel/purchase_return.html",context)

def add_purchase_return(request):
    partys = Party.objects.all()
    fina = Accounting_year.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        bill_no = data["bill_no"]
        party_name = data["party_name"]
        total_amount = data["total_amount"]
        year = data["year"]

        par = Party.objects.get(name=party_name)
        fan = Accounting_year.objects.get(year=year)

        pr = Purchase_Return(
            date = date,
            bill_no = bill_no,
            party_name = par,
            total_amount = total_amount,
            year = fan

        )
        pr.save()   
    return render(request,"arp_panel/add_purchase_return.html",{"party":partys,"fan":fina})

def edit_purchase_return(request,id):
    partys = Party.objects.all()
    fina = Accounting_year.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        bill_no = data["bill_no"]
        party_name = data["party_name"]
        total_amount = data["total_amount"]
        year = data["year"]

        par = Party.objects.get(name=party_name)
        fan = Accounting_year.objects.get(year=year)


        
        r = Purchase_Return.objects.get(pk=id)
        r.date = date
        r.bill_no = bill_no
        r.party_name = par
        r.total_amount = total_amount
        r.year = fan

        r.save()
        return redirect("purchase_return")
    else:
        epr = Purchase_Return.objects.get(pk=id)
    return render(request,"arp_panel/edit_purchase_return.html",{"epr":epr,"party":partys,"fan":fina})

def delete_purchase_return(request,id):
    dpr = Purchase_Return.objects.filter(id=id)
    dpr.delete()
    context = {
        'dpr':dpr,
    }
    return redirect('purchase_return')


def payment_out(request):
    POs = Payment_Out.objects.all()
    context = {
        'po':POs,
    }
    return render(request,"arp_panel/payment_out.html",context)

def add_payment_out(request):
    partys = Party.objects.all()
    bank = BankAccount.objects.all()
    fina = Accounting_year.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        party_name = data["party_name"]
        party_balance = data["party_balance"]
        paid = data["paid"]
        balance_due = data["balance_due"]
        payment_type = data["payment_type"]
        bank_account = data["bank_account"]
        description = data["description"]
        year = data["year"]

        par = Party.objects.get(name=party_name)
        ban = BankAccount.objects.get(name=bank_account)
        fan = Accounting_year.objects.get(year=year)

        po = Payment_Out(
            date = date,
            party_name = par,
            party_balance = party_balance,
            paid = paid,
            balance_due = balance_due,
            payment_type = payment_type,
            bank_account = ban,
            description = description,
            year = fan
            
            )
        po.save()
        return redirect("payment_in")
    return render(request,"arp_panel/add_payment_out.html",{"party":partys,"bank":bank,"fan":fina})

def edit_payment_out(request,id):
    partys = Party.objects.all()
    bank = BankAccount.objects.all()
    fina = Accounting_year.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        party_name = data["party_name"]
        party_balance = data["party_balance"]
        paid = data["paid"]
        balance_due = data["balance_due"]
        payment_type = data["payment_type"]
        bank_account = data["bank_account"]
        description = data["description"]
        year = data["year"]
        

        par = Party.objects.get(name=party_name)
        ban = BankAccount.objects.get(name=bank_account)
        fan = Accounting_year.objects.get(year=year)


        
        o = Payment_Out.objects.get(pk=id)
        o.date = date
        o.party_name = par
        o.party_balance = party_balance
        o.paid = paid
        o.balance_due = balance_due
        o.payment_type = payment_type
        o.bank_account = ban
        o.description = description
        o.year = fan
        

        o.save()
        return redirect("payment_out")
    else:
        epo = Payment_Out.objects.get(pk=id)
    return render(request,"arp_panel/edit_payment_out.html",{"epo":epo,"party":partys,"bank":bank,"fan":fina})

def delete_payment_out(request,id):
    dpo = Payment_Out.objects.filter(id=id)
    dpo.delete()
    context = {
        'dpo':dpo,
    }
    return redirect('payment_out')

def sale_bill(request):
    SB = Sale_Bill.objects.all()
    context = {
        'sb':SB,
    }
    return render(request,"arp_panel/sale_bill.html",context)

def add_sale_invoice(request):
    partys = Party.objects.all()
    fina = Accounting_year.objects.all()
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
        

        sb = Sale_Bill(
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
        return redirect("sale_bill")
    return render(request,"arp_panel/add_sale_invoice.html",{'STATE':STATE,"party":partys,"fan":fina})

def edit_sale_invoice(request,id):
    partys = Party.objects.all()
    fina = Accounting_year.objects.all()
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
        
        s = Sale_Bill.objects.get(pk=id)
        s.date = date
        s.party_name = par
        s.subtotal_amount = subtotal_amount
        s.final_amount = final_amount
        s.payment_type = payment_type
        s.state_of_supply = state_of_supply
        s.description = description
        s.year = fan
        

        s.save()
        return redirect("sale_bill")
    else:
        sbo = Sale_Bill.objects.get(pk=id)
    return render(request,"arp_panel/edit_sale_invoice.html",{"STATE":STATE,"party":partys,"fan":fina,"sbo":sbo})

def delete_sale_invoice(request,id):
    dso = Sale_Bill.objects.filter(id=id)
    dso.delete()
    context = {
        'dso':dso,
    }
    return redirect('sale_bill')



def payment_in(request):
    PI = Payment_In.objects.all()
    context = {
        'pi':PI,
    }
    return render(request,"arp_panel/payment_in.html",context)

def add_payment_in(request):
    partys = Party.objects.all()
    bank = BankAccount.objects.all()
    fina = Accounting_year.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        party_name = data["party_name"]
        party_balance = data["party_balance"]
        opening_balance = data["opening_balance"]
        recieved = data["recieved"]
        balance_due = data["balance_due"]
        payment_type = data["payment_type"]
        bank_account = data["bank_account"]
        description = data["description"]
        year = data["year"]

        par = Party.objects.get(name=party_name)
        ban = BankAccount.objects.get(name=bank_account)
        fan = Accounting_year.objects.get(year=year)

        pi = Payment_In(
            date = date,
            party_name = par,
            party_balance = party_balance,
            opening_balance = opening_balance,
            recieved = recieved,
            balance_due = balance_due,
            payment_type = payment_type,
            bank_account = ban,
            description = description,
            year = fan
            )
        pi.save()
        return redirect("payment_in")
    return render(request,"arp_panel/add_payment_in.html",{"party": partys,"bank":bank,"fan":fina})

def edit_payment_in(request,id):
    partys = Party.objects.all()
    bank = BankAccount.objects.all()
    fina = Accounting_year.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        party_name = data["party_name"]
        party_balance = data["party_balance"]
        opening_balance = data["opening_balance"]
        recieved = data["recieved"]
        balance_due = data["balance_due"]
        payment_type = data["payment_type"]
        bank_account = data["bank_account"]
        description = data["description"]
        year = data["year"]

        par = Party.objects.get(name=party_name)
        ban = BankAccount.objects.get(name=bank_account)
        fan = Accounting_year.objects.get(year=year)


        q = Payment_In.objects.get(pk=id)
        q.date = date
        q.party_name = par
        q.party_balance = party_balance
        q.opening_balance = opening_balance
        q.recieved = recieved
        q.balance_due = balance_due
        q.payment_type = payment_type
        q.bank_account = ban
        q.description = description
        q.year = fan

        q.save()
        return redirect("payment_in")
    else:
        epi = Payment_In.objects.get(pk=id)
    return render(request,"arp_panel/edit_payment_in.html",{"epi":epi,"party":partys,"bank":bank,"fan":fina})

def delete_payment_in(request,id):
    dpi = Payment_In.objects.filter(id=id)
    dpi.delete()
    context = {
        'dpi':dpi,
    }
    return redirect('payment_in')

def sale_return(request):
    SR = Sale_Return.objects.all()
    context = {
        'sr':SR,
    }
    return render(request,"arp_panel/sale_return.html",context)

def add_sale_return(request):
    partys = Party.objects.all()
    fina = Accounting_year.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        bill_no = data["bill_no"]
        party_name = data["party_name"]
        total_sale = data["total_sale"]
        balance = data["balance"]
        year = data["year"]

        par = Party.objects.get(name=party_name)
        fan = Accounting_year.objects.get(year=year)


        sr = Sale_Return(
            date = date,
            party_name = par,
            bill_no = bill_no,
            total_sale = total_sale,
            balance = balance,
            year = fan
            )
        sr.save()
        return redirect("sale_return")
    return render(request,"arp_panel/add_sale_return.html",{"party": partys,"fan":fina})

def edit_sale_return(request,id):
    partys = Party.objects.all()
    fina = Accounting_year.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        bill_no = data["bill_no"]
        party_name = data["party_name"]
        total_sale = data["total_sale"]
        balance = data["balance"]
        year = data["year"]

        par = Party.objects.get(name=party_name)
        fan = Accounting_year.objects.get(year=year)



        t = Sale_Return.objects.get(pk=id)
        t.date = date
        t.party_name = par
        t.bill_no = bill_no
        t.total_sale = total_sale
        t.balance = balance
        t.year = fan


        t.save()
        return redirect("sale_return")
    else:
        esr = Sale_Return.objects.get(pk=id)
    return render(request,"arp_panel/edit_sale_return.html",{"esr":esr,"party":partys,"fan":fina})

def delete_sale_return(request,id):
    dsr = Sale_Return.objects.filter(id=id)
    dsr.delete()
    context = {
        'dsr':dsr,
    }
    return redirect('sale_return')


def expense(request):
    EX = Expense.objects.all()
    context = {
        'ex':EX,
    }
    return render(request,"arp_panel/expense.html",context)

def add_expense(request):
    fina = Accounting_year.objects.all()
    bank = BankAccount.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        expense_category = data["expense_category"]
        total_amount = data["total_amount"]
        payment_type = data["payment_type"]
        bank_account = data["bank_account"]
        description = data["description"]
        year = data["year"]

        ban = BankAccount.objects.get(name=bank_account)
        fan = Accounting_year.objects.get(year=year)


        ex = Expense(
            date = date,
            expense_category = expense_category,
            total_amount = total_amount,
            payment_type = payment_type,
            bank_account = ban,
            description = description,
            year = fan
            )
        ex.save()
        return redirect("expense")
    return render(request,"arp_panel/add_expense.html",{"bank":bank,"fan":fina})

def edit_expense(request,id):
    bank = BankAccount.objects.all()
    fina = Accounting_year.objects.all()
    if request.method == "POST":
        data = request.POST
        date = data["date"]
        expense_category = data["expense_category"]
        total_amount = data["total_amount"]
        payment_type = data["payment_type"]
        bank_account = data["bank_account"]
        description = data["description"]
        year = data["year"]

        ban = BankAccount.objects.get(name=bank_account)
        fan = Accounting_year.objects.get(year=year)

        e = Expense.objects.get(pk=id)
        e.date = date
        e.expense_category = expense_category
        e.total_amount = total_amount
        e.payment_type = payment_type
        e.bank_account = ban
        e.description = description
        e.year = fan


        e.save()
        return redirect("expense")
    else:
        eex = Expense.objects.get(pk=id)
    return render(request,"arp_panel/edit_expense.html",{"eex":eex,"bank":bank,"fan":fina})

def delete_expense(request,id):
    dex = Expense.objects.filter(id=id)
    dex.delete()
    context = {
        'dex':dex,
    }
    return redirect('expense')

def reports(request):
    return render(request,"arp_panel/reports.html")






def sale_report(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Sale_Report.objects.raw('select * from arp_panel_sale_report where date between "'+fromdate+'" and "'+todate+'"' )
        return render(request,"arp_panel/sale_report.html",{"sa": searchresult})
    else:
       SA = Sale_Report.objects.all()
       return render(request,"arp_panel/sale_report.html",{"sa":SA})

    

def new_csv(request):
    response = HttpResponse(content_type = 'text\csv')
    response['Content-Disposition'] = 'attachment; filename=salereports.csv'

    writer =  csv.writer(response)
    sar = Sale_Report.objects.all()

    writer.writerow(['Date','Financial Year','Invoice No','Bill Type','Party Name','Payment Status','Total Amount','Recieved Amount','Balance Amount'])

    for j in sar:
        writer.writerow([j.date,j.year,j.invoice_no,j.bill_type,j.party_name,j.payment_status,j.total_amount,j.recieved_amount,j.balance])

    return response


    

def purchase_report(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Sale_Report.objects.raw('select * from arp_panel_purchase_report where date between "'+fromdate+'" and "'+todate+'"' )
        return render(request,"arp_panel/purchase_report.html",{"pur": searchresult})
    else: 
        PU = Purchase_Report.objects.all()
        return render(request,"arp_panel/purchase_report.html",{"pu": PU})

def new_csv1(request):
    response = HttpResponse(content_type = 'text\csv')
    response['Content-Disposition'] = 'attachment; filename=purchasereports.csv'

    writer =  csv.writer(response)
    puc = Sale_Report.objects.all()

    writer.writerow(['Date','Financial Year','Purchase Bill No','Bill Type','Party Name','Payment Status','Total Amount','Recieved Amount','Balance Amount'])

    for j in puc:
        writer.writerow([j.date,j.year,j.purchase_bill_no,j.bill_type,j.party_name,j.payment_status,j.total_amount,j.recieved_amount,j.balance])

    return response


def daybook(request):
    if request.method == "POST":
        date = request.POST.get('date')
        searchresult = Sale_Report.objects.raw('select * from arp_panel_daybook where date is "'+date+'" and ' )
        return render(request,"arp_panel/daybook.html",{"db": searchresult})
    else: 
        DB = Daybook.objects.all()
        return render(request,"arp_panel/daybook.html",{"db": DB})

def new_csv2(request):
    response = HttpResponse(content_type = 'text\csv')
    response['Content-Disposition'] = 'attachment; filename=daybook.csv'

    writer =  csv.writer(response)
    dab = Daybook.objects.all()

    writer.writerow(['Date','Financial Year','Invoice No','Bill Type','Particulars','Debit','Credit'])

    for j in dab:
        writer.writerow([j.date,j.year,j.invoice_no,j.bill_type,j.particulars,j.debit,j.credit])

    return response


def due_list(request):
   if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Due_List.objects.raw('select * from arp_panel_due_list where date between "'+fromdate+'" and "'+todate+'"' )
        return render(request,"arp_panel/due_list.html",{"dl": searchresult})
   else: 
        DL = Purchase_Report.objects.all()
        return render(request,"arp_panel/due_list.html",{"dl": DL})

def new_csv3(request):
    response = HttpResponse(content_type = 'text\csv')
    response['Content-Disposition'] = 'attachment; filename=due_list.csv'

    writer =  csv.writer(response)
    dul = Due_List.objects.all()

    writer.writerow(['Date','Financial Year','Invoice No','Bill Type','Party Name','Contact Details', 'Payment Status','Total Amount','Recieved Amount','Balance Amount','Employee Name'])

    for j in dul:
        writer.writerow([j.date,j.year,j.invoice_no,j.bill_type,j.party_name,j.payment_status,j.total_amount,j.recieved_amount,j.balance,j.employee_name])

    return response



def stock_summary_report(request):
   if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = Stock_Summary_Report.objects.raw('select * from arp_panel_stock_summary_report where date between "'+fromdate+'" and "'+todate+'"' )
        return render(request,"arp_panel/stock_summary_report.html",{"dl": searchresult})
   else: 
        SSR = Stock_Summary_Report.objects.all()
        return render(request,"arp_panel/stock_summary_report.html",{"ssr": SSR})

def new_csv4(request):
    response = HttpResponse(content_type = 'text\csv')
    response['Content-Disposition'] = 'attachment; filename=stock_summary_report.csv'

    writer =  csv.writer(response)
    sse = Stock_Summary_Report.objects.all()

    writer.writerow(['Date','Financial Year','Item Name','Sale Price','Purchase Price','Stock Qty', 'Stock Value'])

    for j in sse:
        writer.writerow([j.date,j.year,j.item_name,j.sale_price,j.purchase_price,j.stock_qty,j.stock_value])

    return response





def gstr1(request):
   if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = GSTR1.objects.raw('select * from arp_panel_gstr1 where date between "'+fromdate+'" and "'+todate+'"' )
        return render(request,"arp_panel/gstr1.html",{"dl": searchresult})
   else: 
        GST1 = GSTR1.objects.all()
        return render(request,"arp_panel/gstr1.html",{"gst1": GST1})

def new_csv5(request):
    response = HttpResponse(content_type = 'text\csv')
    response['Content-Disposition'] = 'attachment; filename=gstr1report.csv'

    writer =  csv.writer(response)
    gst1 = GSTR1.objects.all()

    writer.writerow(['Date','Financial Year','HSN','Description','UQC','Taxable Value', 'Integrated Tax Amount','Central Tax Amount','State UI Tax Amount','CESS Amount'])

    for j in gst1:
        writer.writerow([j.date,j.year,j.hsn,j.description,j.uqc,j.taxable_value,j.integrated_tax_amount,j.central_tax_amount,j.state_ui_tax_amount,j.cess_amount])

    return response

def gstr2(request):
    GST2 = GSTR2.objects.all()
    context = {
        "gstr2": GST2
    }
    return render(request,"arp_panel/gstr2.html",context)

def gstr3b(request):
   if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        searchresult = GSTR3B.objects.raw('select * from arp_panel_gstr3b where date between "'+fromdate+'" and "'+todate+'"' )
        return render(request,"arp_panel/gstr3b.html",{"gst2": searchresult})
   else: 
        GST3 = GSTR3B.objects.all()
        return render(request,"arp_panel/gstr3b.html",{"gst3": GST3})

def new_csv7(request):
    response = HttpResponse(content_type = 'text\csv')
    response['Content-Disposition'] = 'attachment; filename=gstr3b.csv'

    writer =  csv.writer(response)
    gst3 = GSTR3B.objects.all()

    writer.writerow(['Date','Financial Year','Inter State Supplies','Intra State Supplies'])

    for j in gst3:
        writer.writerow([j.date,j.year,j.hsn,j.description,j.uqc,j.taxable_value,j.integrated_tax_amount,j.central_tax_amount,j.state_ui_tax_amount,j.cess_amount])

    return response


def add_items(request):
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
    return render(request,"arp_panel/add_items.html",{"prd": prods, "ser": servs})


def edit_product(request, id):
    ep = Product.objects.get(pk=id)
    prods = Product.objects.all()
    return render(request, "arp_panel/add_items.html", {'ep':ep,"prd": prods})





def add_items1(request):
    prods1 = Product.objects.all()
    servs1 = Service.objects.all()
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
    return render(request,"arp_panel/add_items1.html",{"prd1": prods1, "ser1": servs1})


def edit_product1(request, id):
    ep1 = Product.objects.get(pk=id)
    prods1 = Product.objects.all()
    return render(request, "arp_panel/add_items1.html", {'ep1':ep1,"prd1": prods1})


def edit_add_items(request):
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
    return render(request,"arp_panel/edit_purchase_add_items.html",{"prd": prods, "ser": servs})


def edit_add_product(request, id):
    ep = Product.objects.get(pk=id)
    prods = Product.objects.all()
    return render(request, "arp_panel/edit_purchase_add_items.html", {'ep':ep,"prd": prods})


def edit_add_items1(request):
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
    return render(request,"arp_panel/edit_sale_invoice_add_items.html",{"prd": prods, "ser": servs})


def edit_add_product1(request, id):
    sbo = Product.objects.get(pk=id)
    prods = Product.objects.all()
    return render(request, "arp_panel/edit_sale_invoice_add_items.html", {'sbo':sbo,"prd": prods})

def due_challan(request):
    dch = Sale_Challan.objects.all()
    context = {
        'dc':dch,
    }
    return render(request,"arp_panel/due_challan.html",context)

        
    


