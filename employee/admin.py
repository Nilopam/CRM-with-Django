from django.contrib import admin
from . models import *
# Register your models here.


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ("id", "emp", "date", "in_time", "status","half")
#     list_filter = ("date", "status", "half","emp")


my_models = [Emp,Notice,
TravelAllow,Resignation,LeaveApproval,Attendance,Payslip,Leaders]
admin.site.register(my_models)

# admin.site.register(Attendance, ProfileAdmin)
