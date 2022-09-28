
from django import views
from django.urls import path
from . import views

urlpatterns = [

    path("purchase_bill/",views.purchase_bill, name="purchase_bill"),
    path("add_purchase/",views.add_purchase, name="add_purchase"),
    path("edit_purchase/<int:id>",views.edit_purchase, name="edit_purchase"),
    path("delete_purchase/<int:id>",views.delete_purchase, name="delete_purchase"),

    path("purchase_return/",views.purchase_return, name="purchase_return"),
    path("add_purchase_return/",views.add_purchase_return, name="add_purchase_return"),
    path("edit_purchase_return/<int:id>",views.edit_purchase_return, name="edit_purchase_return"),
    path("delete_purchase_return/<int:id>",views.delete_purchase_return, name="delete_purchase_return"),

    path("payment_out/",views.payment_out, name="payment_out"),
    path("add_payment_out/",views.add_payment_out, name="add_payment_out"),
    path("edit_payment_out/<int:id>",views.edit_payment_out, name="edit_payment_out"),
    path("delete_payment_out/<int:id>",views.delete_payment_out, name="delete_payment_out"),


    path("sale_bill/",views.sale_bill, name="sale_bill"),
    path("add_sale_invoice/",views.add_sale_invoice, name="add_sale_invoice"),
    path("edit_sale_invoice/<int:id>",views.edit_sale_invoice, name="edit_sale_invoice"),
    path("delete_sale_invoice/<int:id>",views.delete_sale_invoice, name="delete_sale_invoice"),


    path("payment_in/",views.payment_in, name="payment_in"),
    path("add_payment_in/",views.add_payment_in, name="add_payment_in"),
    path("edit_payment_in/<int:id>",views.edit_payment_in, name="edit_payment_in"),
    path("delete_payment_in/<int:id>",views.delete_payment_in, name="delete_payment_in"),

    path("sale_return/",views.sale_return, name="sale_return"),
    path("add_sale_return/",views.add_sale_return, name="add_sale_return"),
    path("edit_sale_return/<int:id>",views.edit_sale_return, name="edit_sale_return"),
    path("delete_sale_return/<int:id>",views.delete_sale_return, name="delete_sale_return"),

    path("expense/",views.expense, name="expense"),
    path("add_expense/",views.add_expense, name="add_expense"),
    path("edit_expense/<int:id>",views.edit_expense, name="edit_expense"),
    path("delete_expense/<int:id>",views.delete_expense, name="delete_expense"),

    path("reports/",views.reports, name="reports"),
    path("sale_report/",views.sale_report, name="sale_report"),
    path("new_csv/",views.new_csv, name="new_csv"),
    path("purchase_report/",views.purchase_report, name="purchase_report"),
    path("new_csv1/",views.new_csv1, name="new_csv1"),
    path("daybook/",views.daybook, name="daybook"),
    path("new_csv2/",views.new_csv2, name="new_csv2"),
    path("due_list/",views.due_list, name="due_list"),
    path("new_csv3/",views.new_csv3, name="new_csv3"),
    path("stock_summary_report/",views.stock_summary_report, name="stock_summary_report"),
    path("new_csv4/",views.new_csv4, name="new_csv4"),

    path("gstr1/",views.gstr1, name="gstr1"),
    path("new_csv5/",views.new_csv5, name="new_csv5"),
    path("gstr2/",views.gstr2, name="gstr2"),
    path("gstr3b/",views.gstr3b, name="gstr3b"),
    path("new_csv7/",views.new_csv7, name="new_csv7"),

    path("add_items/",views.add_items, name="add_items"),
    path("add_items/<int:id>",views.edit_product, name="add_items"),
    path("edit_add_items/",views.edit_add_items, name="edit_add_items"),
    path("edit_add_items/<int:id>",views.edit_add_product, name="edit_add_items"),
    
    path("add_items1/",views.add_items1, name="add_items1"),
    path("add_items1/<int:id>",views.edit_product1, name="add_items1"),
    path("edit_add_items1/",views.edit_add_items1, name="edit_add_items1"),
    path("edit_add_items1/<int:id>",views.edit_add_product1, name="edit_add_items1"),

    path("due_challan/",views.due_challan, name="due_challan"),
    
    

    




 


]