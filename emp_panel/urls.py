from django.urls import path
from . import views

urlpatterns = [

    
    path("emp_dash",views.emp_dash,name="emp_dash"),
    path("my_profile",views.my_profile,name="my_profile"),
    path("leave_application",views.leave_application,name="leave_application"),

    path("apply_resignation",views.apply_resignation,name="apply_resignation"),

    path("apply_travel_allow",views.apply_travel_allow,name="apply_travel_allow"),

    path("emp_attendance",views.emp_attendance,name="emp_attendance"),

    path("emp_payslip",views.emp_payslip,name="emp_payslip"),

    path("emp_travel",views.emp_travel,name="emp_travel"),
    path("emp_travel_approve/<int:id>",views.emp_travel_approve,name="emp_travel_approve"),
    path("emp_travel_reject/<int:id>",views.emp_travel_reject,name="emp_travel_reject"),


    path("sub_emp_attendance",views.sub_emp_attendance,name="sub_emp_attendance"),
    path("sub_makehalf/<int:id>",views.sub_makehalf,name="sub_makehalf"),
    path("sub_makefull/<int:id>",views.sub_makefull,name="sub_makefull"),
    path("sub_reject_attendance/<int:id>",views.sub_reject_attendance,name="sub_reject_attendance"),

    
    path("sub_leave_approval",views.sub_leave_approval,name="sub_leave_approval"),
    path("sub_leave_approval_approve/<int:id>",views.sub_leave_approval_approve,name="sub_leave_approval_approve"),
    path("sub_leave_approval_reject<int:id>",views.sub_leave_approval_reject,name="sub_leave_approval_reject"),

    path("sub_add_daily_work",views.sub_add_daily_work,name="sub_add_daily_work"),
    path("sub_daily_report/",views.sub_daily_report,name="sub_daily_report"),
    path("sub_daily_report_approve/<int:id>",views.sub_daily_report_approve,name="sub_daily_report_approve"),
    
]