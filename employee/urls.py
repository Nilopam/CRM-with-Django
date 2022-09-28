from django.urls import path
from . import views

urlpatterns = [
    # path("",views.login,name="login"),

    # employee crud views starts 
    path("create_emp/",views.create_emp,name="create_emp"),
    path("show_emp/",views.show_emp,name="show_emp"),
    path("delete_emp/<int:id>",views.delete_emp,name="delete_emp"),
    path("update_emp/<int:id>",views.update_emp,name="update_emp"),
    # employee crud views ends

    path("travel/",views.travel,name="travel"),
    path("travel_approve/<int:id>",views.travel_approve,name="travel_approve"),
    path("travel_reject/<int:id>",views.travel_reject,name="travel_reject"),



    
    path("attendance/",views.attendance,name="attendance"),
    path("reject_attendance/<int:id>",views.reject_attendance,name="reject_attendance"),
    path("makefull/<int:id>",views.makefull,name="makefull"),
    path("makehalf/<int:id>",views.makehalf,name="makehalf"),
    



    path("custom_attendance/",views.custom_attendance,name="custom_attendance"),



    path("payslip/",views.payslip,name="payslip"),
    

    path("leave_approval/",views.leave_approval,name="leave_approval"),
    path("leave_approval_approve/<int:id>",views.leave_approval_approve,name="leave_approval_approve"),
    path("leave_approval_reject/<int:id>",views.leave_approval_reject,name="leave_approval_reject"),


    path("notice/",views.notice,name="notice"),
    path("notice_add/",views.notice_add,name="notice_add"),
    path("notice_edit/<int:id>",views.notice_edit,name="notice_edit"),
    path("notice_delete/<int:id>",views.notice_delete,name="notice_delete"),


    path("resignation/",views.resignation,name="resignation"),
    path("resignation_approve/<int:id>",views.resignation_approve,name="resignation_approve"),
    path("resignation_reject/<int:id>",views.resignation_reject,name="resignation_reject"),



]
