
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import DailyReport
from admin_panel.models import Party
from employee.models import Emp

# Create your views here.
def daily_report(request):
    partys = Party.objects.all()
    emps = Emp.objects.all()
    if request.method == "POST":
        data = request.POST
        party_name = data['party']
        emp_name = data['emp']
        if party_name:
            daily_reports = DailyReport.objects.filter(party = party_name)
            context={
                "daily_reports":daily_reports,
                "emps":emps,
            "partys":partys,
            }
            return render(request,"daily_report.html",context)
        if emp_name:
            daily_reports = DailyReport.objects.filter(emp = emp_name)
            context={
                "daily_reports":daily_reports,
                "emps":emps,
            "partys":partys,
            }
            return render(request,"daily_report.html",context)

    daily_reports =  DailyReport.objects.all()    
    context = {
            "daily_reports":daily_reports,
            "emps":emps,
            "partys":partys,
        }
    return render(request,"daily_report.html",context)

def daily_report_approve(request,id):
    if DailyReport.objects.get(pk=id):
        daily_report =  DailyReport.objects.get(pk=id)
        daily_report.approved = True
        daily_report.save()

        return redirect("daily_report")
    return HttpResponse("Not Present")


