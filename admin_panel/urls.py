
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    # path("login",views.login, name="login"),
    # path("my_profile/",views.my_profile, name="my_profile"),

  


    # path("my_customer/",views.my_customer, name="my_customer"),
    # path("add_customer/",views.add_customer, name="add_customer"),

    # path("place_order/",views.place_order, name="place_order"),
    # path("add_place_order/",views.add_place_order, name="add_place_order"),
    # path("view_place_order/",views.view_place_order, name="view_place_order"),
    # path("cancel_order/",views.cancel_order, name="cancel_order"),

    # path("cancel_order_report/",views.cancel_order_report, name="cancel_order_report"),
    
    # path("party_ledger/",views.party_ledger, name="party_ledger"),
    # path("party_details/",views.party_details, name="party_details"),
    
    # path("cylinder_delivery_report/",views.cylinder_delivery_report, name="cylinder_delivery_report"),
    
    
    # path("designation/",views.designation,name="designation"),
    path("designation/",views.designation, name="designation"),
    path("designation_add/",views.designation_add, name="designation_add"),
    path("designation_edit/<int:id>",views.designation_edit, name="designation_edit"),
    path("designation_delete/<int:id>",views.designation_delete, name="designation_delete"),
    
    path("place/",views.place,name="place"),
    path("place_add/",views.place_add,name="place_add"),
    path("place_edit/<int:id>",views.place_edit,name="place_edit"),
    path("place_delete/<int:id>",views.place_delete,name="place_delete"),

    path("holiday/",views.holiday,name="holiday"),
    path("holiday_add/",views.holiday_add,name="holiday_add"),
    path("holiday_edit/<int:id>",views.holiday_edit,name="holiday_edit"),
    path("holiday_delete/<int:id>",views.holiday_delete,name="holiday_delete"),

    path("accounting_year/",views.accounting_year,name="accounting_year"),
    path("accounting_year_add/",views.accounting_year_add,name="accounting_year_add"),
    path("accounting_year_edit/<int:id>",views.accounting_year_edit,name="accounting_year_edit"),
    path("accounting_year_delete/<int:id>",views.accounting_year_delete,name="accounting_year_delete"),
   
   
    path("arp_items/",views.arp_items,name="arp_items"),
    path("product_add/",views.product_add,name="product_add"),
    path("product_edit/<int:id>",views.product_edit,name="product_edit"),
    path("product_delete/<int:id>",views.product_delete,name="product_delete"),

    path("service_add/",views.service_add,name="service_add"),
    path("service_edit/<int:id>",views.service_edit,name="service_edit"),
    path("service_delete/<int:id>",views.service_delete,name="service_delete"),


    path("prp_service_add/",views.prp_service_add,name="prp_service_add"),
    # path("arp_service_edit/<int:id>",views.arp_service_edit,name="arp_service_edit"),




    path("arp_party/",views.arp_party,name="arp_party"),
    path("arp_party_add/",views.arp_party_add,name="arp_party_add"),
    path("arp_party_edit/<int:id>",views.arp_party_edit,name="arp_party_edit"),
    path("arp_party_delete/<int:id>",views.arp_party_delete,name="arp_party_delete"),



    path("prp_party/",views.prp_party,name="prp_party"),
    path("prp_party_add/",views.prp_party_add,name="prp_party_add"),
    path("prp_party_edit/<int:id>",views.prp_party_edit,name="prp_party_edit"),
    path("prp_party_delete/<int:id>",views.prp_party_delete,name="prp_party_delete"),


    path("bank_list/",views.bank_list,name="bank_list"),
    path("bank_add/",views.bank_add,name="bank_add"),
    path("bank_delete/<int:id>",views.bank_delete,name="bank_delete"),


    path("item_category/",views.item_category,name="item_category"),
    path("item_category_add/",views.item_category_add,name="item_category_add"),
    path("item_category_edit/<int:id>",views.item_category_edit,name="item_category_edit"),
    path("item_category_delete/<int:id>",views.item_category_delete,name="item_category_delete"),


    path("expense_item/",views.expense_item,name="expense_item"),
    path("expense_item_add/",views.expense_item_add,name="expense_item_add"),
    path("expense_item_edit/<int:id>",views.expense_item_edit,name="expense_item_edit"),
    path("expense_item_delete/<int:id>",views.expense_item_delete,name="expense_item_delete"),


    path("expense_category/",views.expense_category,name="expense_category"),
    path("expense_category_add/",views.expense_category_add,name="expense_category_add"),
    path("expense_category_edit/<int:id>",views.expense_category_edit,name="expense_category_edit"),
    path("expense_category_delete/<int:id>",views.expense_category_delete,name="expense_category_delete"),



]
