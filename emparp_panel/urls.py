from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("emp_sale_billings/",views.emp_sale_billings, name="emp_sale_billings"),
    path("emp_add_sale_invoice/",views.emp_add_sale_invoice, name="emp_add_sale_invoice"),
    path("emp_edit_sale_invoice/<int:id>",views.emp_edit_sale_invoice, name="emp_edit_sale_invoice"),
    path("emp_delete_sale_invoice/<int:id>",views.emp_delete_sale_invoice, name="emp_delete_sale_invoice"),

    path("emp_sale_return/",views.emp_sale_return, name="emp_sale_return"),
    path("emp_add_sale_return/",views.emp_add_sale_return, name="emp_add_sale_return"),
    path("emp_edit_sale_return/<int:id>",views.emp_edit_sale_return, name="emp_edit_sale_return"),
    path("emp_delete_sale_return/<int:id>",views.emp_delete_sale_return, name="emp_delete_sale_return"),

    path("emp_sale_challan/",views.emp_sale_challan, name="emp_sale_challan"),
    path("emp_add_sale_challan/",views.emp_add_sale_challan, name="emp_add_sale_challan"),
    path("emp_edit_sale_challan/<int:id>",views.emp_edit_sale_challan, name="emp_edit_sale_challan"),
    path("emp_delete_sale_challan/<int:id>",views.emp_delete_sale_challan, name="emp_delete_sale_challan"),

    path("emp_add_items/",views.emp_add_items, name="emp_add_items"),
    path("emp_add_items/<int:id>",views.emp_edit_product, name="emp_add_items"),
    path("emp_add_items1/",views.emp_add_items1, name="emp_add_items1"),
    path("emp_add_items1/<int:id>",views.emp_edit_product1, name="emp_add_items1"),

   
    path("emp_edit_add_items/",views.emp_edit_add_items, name="emp_edit_add_items"),
    path("emp_edit_add_items/<int:id>",views.emp_edit_add_product, name="emp_edit_add_items"),

]