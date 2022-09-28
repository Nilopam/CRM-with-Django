from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from employee.models import LeaveApproval,Emp,Resignation,TravelAllow,Payslip
from employee.models import Attendance
from employee.models import  Leaders
from django.http import HttpResponse
from employee.forms import *
from admin_panel.models import Party
from dailyreport.models import DailyReport
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.

@login_required
def emp_dash(request):

    return render(request,"empbase.html")


@login_required
def leave_application(request):
    emp = Emp.objects.get(name = request.user.first_name)
    leaves = LeaveApproval.objects.filter(emp = emp.id).order_by('-created_at')
    
    if request.method == "POST":
        if request.POST['form-type'] == "add": 
            data = request.POST
            from_date = data['from_date']
            to_date = data['to_date']
            categor = data['category']
            reason = data['reason']
            empid = Emp.objects.get(id= emp.id)

            from_date = datetime.datetime.strptime(from_date, '%Y/%m/%d').date()
            to_date = datetime.datetime.strptime(to_date, '%Y/%m/%d').date()
            obj = LeaveApproval(emp = empid,from_date=from_date,to_date=to_date
            ,category = categor ,reason=reason)

            obj.save()
            return redirect("leave_application")
        if request.POST['form-type'] == "filter":
            fromdate = request.POST['fromdate']
            category = request.POST['category']
            print(fromdate)
            print(category)
            if not fromdate == "":
                year = int(fromdate[:4])
                month = int(fromdate[5:7])

                date = int(fromdate[8:])

            if(fromdate!= "" or category != ""):
                if(fromdate !=""):
                    leaves = leaves.filter(from_date__gte=datetime.date (2022,1, 1), from_date__lte=datetime.date (year, month, date)).order_by('-created_at')
                if(category != ""):
                    leaves = leaves.filter(category=category).order_by('-created_at')
            if(fromdate!= "" and category != ""):
                leaves = leaves.filter(from_date__gte=datetime.date (2022,1, 1), from_date__lte=datetime.date (year, month, date),category=category).order_by('-created_at')
        # context = {
        #         "leaves" : leaves,
                
        #     }
    context = {
            "leaves" : leaves,
            'category' : LeaveApproval.Category
        }



    
    return render(request,"leave_application.html",context)



@login_required
def apply_resignation(request):

    empid = Emp.objects.get(name = request.user.first_name)
    resignations = Resignation.objects.filter(emp = empid).order_by('-created_at')
    if request.method == "POST":
        data = request.POST
        reason = data['reason']
        empid = Emp.objects.get(id= empid.id)

        obj = Resignation(emp = empid,reason = reason)
        obj.save()
        return redirect("apply_resignation")

    context = {
        "resignations":resignations
    }
    return render(request,"apply_resignation.html",context)



@login_required
def apply_travel_allow(request):
    empid = Emp.objects.get(name= request.user.first_name)
    tas = TravelAllow.objects.filter(emp = empid).order_by('-date')
    if request.method == "POST":
        if request.POST['form-type'] == "add":

            data = request.POST
            from_where = data['from_where']
            destination = data['destination']
            date = data['date']
            expense = data['expense']
            distance = data['distance']
            purpose = data['purpose']
            remarks = data['remarks']
            empid = Emp.objects.get(id= empid.id)
            obj = TravelAllow(emp = empid,date=date,from_where=from_where,
            destination=destination,distance=distance,expense=expense,purpose=purpose,
            remarks=remarks)

            obj.save()
            print(f"{empid} applied TA")
            return redirect("apply_travel_allow")
        if request.POST['form-type'] == "filter":

            from_date = request.POST['from_date']
            to_date = request.POST['to_date']
            if from_date != "" and to_date != "": #checking that both dates are not empty and later getting dates
                from_dateyear = int(from_date[:4])
                from_datemonth = int(from_date[5:7])
                from_datedate = int(from_date[8:])
                to_dateyear = int(to_date[:4])
                to_datemonth = int(to_date[5:7])
                to_datedate = int(to_date[8:])

                tas = tas.filter(date__gte=datetime.date (from_dateyear,from_datemonth, from_datedate), 
                            date__lte=datetime.date (to_dateyear, to_datemonth, to_datedate)).order_by('-date')
            


            


    
    

       
    context = {
        "tas":tas
    }
    return render(request,"apply_travel_allow.html",context)



@login_required
def emp_attendance(request):

    emp = Emp.objects.get(name = request.user.first_name)
    
    attendances = Attendance.objects.filter(emp = emp.id)

    context = {
        "attendances" :attendances
    }

    return render(request,"emp_attendance.html",context)


@login_required
def emp_payslip(request):
    emp = Emp.objects.get(name = request.user.first_name)

    payslips = Payslip.objects.filter(emp = emp.id)
    context = {
        "payslips" :payslips
    }
    return render(request,"emp_payslip.html",context)





@login_required
def emp_travel(request):
    emp = Emp.objects.get(name = request.user.first_name)

    if Leaders.objects.filter(leaderid = emp.id).exists():
        
        leaderid = Leaders.objects.get(leaderid = emp.id)
        print(leaderid,"is team leader!!".upper())
        subEmps = Emp.objects.filter(under_of=leaderid.id)
        print(subEmps,"are employees that comes under!!".upper())

        ls = []
        for i in subEmps:
            ls.append(i.id)
            print(i.id)

        transports = TravelAllow.objects.filter(emp_id__in=ls)
        if request.method == "POST":
            employee = request.POST['employee']
            from_date = request.POST['from_date']
            to_date = request.POST['to_date']
            if from_date != "" and to_date != "": #checking that both dates are not empty and later getting dates
                from_dateyear = int(from_date[:4])
                from_datemonth = int(from_date[5:7])
                from_datedate = int(from_date[8:])
                to_dateyear = int(to_date[:4])
                to_datemonth = int(to_date[5:7])
                to_datedate = int(to_date[8:])

            if (employee != "" or from_date!= "" or to_date != ""):
                if(employee != ""):
                    transports =  transports.filter(emp_id = employee)
                elif(from_date != "" and to_date != ""):
                    transports = transports.filter(date__gte=datetime.date (from_dateyear,from_datemonth, from_datedate),
                date__lte=datetime.date (to_dateyear, to_datemonth, to_datedate))
            if (employee != "" and from_date!= "" and to_date != ""):

                transports = transports.filter(
                    emp_id = employee,
                    date__gte=datetime.date (from_dateyear,from_datemonth, from_datedate),
                    date__lte=datetime.date (to_dateyear, to_datemonth, to_datedate)
                ).order_by('-date')


        
        return render(request,"emp_travel.html",{'transports':transports,'employee':subEmps})
    else:
        return HttpResponse("Cant Access this page Coz you are not a leader!!".upper())

@login_required
def emp_travel_approve(request,id):
    emp = Emp.objects.get(name = request.user.first_name)
    if Leaders.objects.filter(leaderid = emp.id).exists():
        if TravelAllow.objects.get(pk=id):
            leave = TravelAllow.objects.get(pk=id)
            if  leave.status == "R" or leave.status=="P":
                leave.status = "A"
                leave.save()
                return redirect("emp_travel")
            else:
                return HttpResponse("its already Aprooved")
        return HttpResponse("Not Present")
    else:
        return HttpResponse("Cant Access this page Coz you are not a leader!!".upper())

@login_required
def emp_travel_reject(request,id):
    emp = Emp.objects.get(name = request.user.first_name)

    if Leaders.objects.filter(leaderid = emp.id).exists(): 
        if TravelAllow.objects.get(pk=id):
            leave = TravelAllow.objects.get(pk=id)
            if  leave.status == "A" or leave.status=="P":
                leave.status = "R"
                leave.save()
                return redirect("emp_travel")
            else:
                return HttpResponse("its already Rejected")
        return HttpResponse("Not Present")
    else:
        return HttpResponse("Cant Access this page Coz you are not a leader!!".upper())


@login_required
def sub_emp_attendance(request):
    emp = Emp.objects.get(name = request.user.first_name)

    if Leaders.objects.filter(leaderid = emp.id).exists():
        emp = Emp.objects.get(name = request.user.first_name)
        leaderid = Leaders.objects.get(leaderid = emp.id)
        print(leaderid)

        subEmps = Emp.objects.filter(under_of=leaderid.id)

        print(subEmps)
        ls = []
        for i in subEmps:
            ls.append(i.id)
            print(i.id)

        attendances = Attendance.objects.filter(emp_id__in=ls)
        return render(request,"sub_emp_attendance.html",{"attendances":attendances})
    else:
        return HttpResponse("Cant Access this page Coz you are not a leader!!".upper())

@login_required
def sub_reject_attendance(request,id):
    emp = Emp.objects.get(name = request.user.first_name)

    if Leaders.objects.filter(leaderid = emp.id).exists():
        if Attendance.objects.get(pk=id):
            attendance = Attendance.objects.get(pk=id)
            if attendance.status == "A":
                attendance.status = "R"
                attendance.save()
                return redirect("sub_emp_attendance")
            if attendance.status == "R":
                return HttpResponse("Already Rejected")
            
        return HttpResponse("Not Present")
    else:
        return HttpResponse("Cant Access this page Coz you are not a leader!!".upper())
@login_required
def sub_makefull(request,id):
    emp = Emp.objects.get(name = request.user.first_name)

    if Leaders.objects.filter(leaderid = emp.id).exists():
        if Attendance.objects.get(pk=id):
            attendance = Attendance.objects.get(pk=id)
            if attendance.half:
                attendance.half = False
                attendance.save()
                return redirect("sub_emp_attendance")
            else:
                return HttpResponse("its already Full")
        return HttpResponse("Not Present")
    else:
        return HttpResponse("Cant Access this page Coz you are not a leader!!".upper())
@login_required
def sub_makehalf(request,id):
    emp = Emp.objects.get(name = request.user.first_name)

    if Leaders.objects.filter(leaderid = emp.id).exists():
        if Attendance.objects.get(pk=id):
            attendance = Attendance.objects.get(pk=id)
            if not attendance.half:
                attendance.half = True
                attendance.save()
                return redirect("sub_emp_attendance")
            else:
                return HttpResponse("its already Half")
        return HttpResponse("Not Present")
    else:
        return HttpResponse("Cant Access this page Coz you are not a leader!!".upper())



@login_required
def sub_leave_approval(request):
    emp = Emp.objects.get(name = request.user.first_name)

    if Leaders.objects.filter(leaderid = emp.id).exists():
    # emp = Emp.objects.get(name = request.user.first_name)
        leaderid = Leaders.objects.get(leaderid = emp.id)
        print(leaderid)

        subEmps = Emp.objects.filter(under_of=leaderid.id)

        print(subEmps)
        ls = []
        for i in subEmps:
            ls.append(i.id)
            print(i.id)

        leaves = LeaveApproval.objects.filter(emp_id__in=ls)
        if request.method == "POST":
            employee = request.POST['employee']
            category = request.POST['category']
            from_date = request.POST['from_date']
            to_date = request.POST['to_date']
            if from_date != "" and to_date != "": #checking that both dates are not empty and later getting dates
                from_dateyear = int(from_date[:4])
                from_datemonth = int(from_date[5:7])
                from_datedate = int(from_date[8:])
                to_dateyear = int(to_date[:4])
                to_datemonth = int(to_date[5:7])
                to_datedate = int(to_date[8:])
            if (employee != "" or category!= "" or from_date!= "" or to_date != ""):
                if(employee != "" and category == "" and from_date == "" and to_date == ""): #doing for emp 
                    leaves = leaves.filter(emp_id = employee)

                elif(employee != "" and category!= "" and from_date == "" and to_date == "" ): #doing for emp and category
                    leaves = leaves.filter(emp_id = employee,category = category)

                elif(employee != "" and from_date != "" and to_date != ""):#doing for emp and dates
                    leaves = leaves.filter(emp_id = employee,from_date__gte=datetime.date (from_dateyear,from_datemonth, from_datedate),
                    from_date__lte=datetime.date (to_dateyear, to_datemonth, to_datedate))

                elif(category!= "" and from_date != "" and to_date != ""): #doing for category and dates
                    leaves = leaves.filter(from_date__gte=datetime.date (from_dateyear,from_datemonth, from_datedate),
                    from_date__lte=datetime.date (to_dateyear, to_datemonth, to_datedate),category = category)

                elif(from_date != "" and to_date != ""):#doing for dates 
                    leaves = leaves.filter(from_date__gte=datetime.date (from_dateyear,from_datemonth, from_datedate),
                    from_date__lte=datetime.date (to_dateyear, to_datemonth, to_datedate))

                elif(category != ""):#doing for category 
                    leaves = leaves.filter(category = category)

            if (employee != "" and category!= "" and from_date!= "" and to_date != ""):
                leaves = leaves.filter(emp_id = employee,category=category,
                from_date__gte=datetime.date (from_dateyear,from_datemonth, from_datedate),
                    from_date__lte=datetime.date (to_dateyear, to_datemonth, to_datedate))

        return render(request, "sub_leave_approval.html",{"leaves":leaves,"employee":subEmps})
    else:
        return HttpResponse("Cant Access this page Coz you are not a leader!!".upper())

@login_required
def sub_leave_approval_approve(request,id):
    emp = Emp.objects.get(name = request.user.first_name)

    if Leaders.objects.filter(leaderid = emp.id).exists():
        if LeaveApproval.objects.get(pk=id):
            leave = LeaveApproval.objects.get(pk=id)
            if  leave.status == "R" or leave.status=="P":
                leave.status = "A"
                leave.save()
                return redirect("sub_leave_approval")
            else:
                return HttpResponse("its already Aprooved")
        return HttpResponse("Not Present")
    else:
        return HttpResponse("Cant Access this page Coz you are not a leader!!".upper())
    
    



@login_required
def sub_leave_approval_reject(request,id):
    emp = Emp.objects.get(name = request.user.first_name)

    if Leaders.objects.filter(leaderid = emp.id).exists():
        if LeaveApproval.objects.get(pk=id):
            leave = LeaveApproval.objects.get(pk=id)
            if not leave.status == "R" or leave.status=="P":
                leave.status = "R"
                leave.save()
                return redirect("sub_leave_approval")
            else:
                return HttpResponse("its already Rejected")
        return HttpResponse("Not Present")
    else:
        return HttpResponse("Cant Access this page Coz you are not a leader!!".upper())


@login_required
def my_profile(request):
    emp = Emp.objects.get(name = request.user.first_name)
    empid  = Emp.objects.get(pk=emp.id)
    Empform = EmpForm(instance=empid)

    
    return render(request,"my_profile.html",{'Empform':Empform
    })




@login_required
def sub_add_daily_work(request):
    
    
    print(request.user.first_name)
    emp = Emp.objects.get(name = request.user.first_name)
    print(emp.id)
    
    partys = Party.objects.all()
    reports = DailyReport.objects.filter(emp = emp.id).order_by('-workdate')
    if request.method == "POST":
        if request.POST['form-type'] == "add":
            data = request.POST
            party = Party.objects.get(id = data['party'])

            empid = Emp.objects.get(id = emp.id)
            work_detail = data['work_detail']

            
            obj = DailyReport(emp= empid,party=party,work_detail=work_detail)
            obj.save()
            return redirect("sub_add_daily_work")
        
        if request.POST['form-type'] == "filter":
            party = request.POST['party']
            workdate = request.POST['workdate']
            if not workdate == "":
                year = int(workdate[:4])
                month = int(workdate[5:7])

                date = int(workdate[8:])
            
            if (party != "" or workdate != ""):
                if (party != ""):
                    reports = reports.filter(party=party).order_by('-workdate')
                elif (workdate != ""):
                    reports =  reports.filter(created_at__gte=datetime.date (2022,1, 1), created_at__lte=datetime.date (year, month, date)).order_by('-workdate')
            

            if (party != "" and workdate != ""):
                reports =  DailyReport.objects.filter(party=party,created_at__gte=datetime.date (2022,1, 1), created_at__lte=datetime.date (year, month, date)).order_by('-workdate')


                

    
    return render(request,"sub_add_daily_work.html",{"partys":partys,"reports":reports})


@login_required
def sub_daily_report(request):
    emp = Emp.objects.get(name = request.user.first_name)

    if Leaders.objects.filter(leaderid = emp.id).exists(): #checking if the employee is leader or not
        partys = Party.objects.all()
        # emp = Emp.objects.get(name = request.user.first_name)
        print(emp.id)
        leaderid = Leaders.objects.get(leaderid = emp.id)#geting leader instance in leaders table from employee id
        subEmps = Emp.objects.filter(under_of=leaderid.id)#getting all emps that belong to a leader
        
        print(subEmps)

        ls = []
        if request.method == "POST":    #if filter request then 
            party = request.POST['party']
            emp = request.POST['emp']
            workdate = request.POST['workdate']
            
            year = int(workdate[:4])
            month = int(workdate[5:7])
            date = int(workdate[8:])
            print(date)
            
            for i in subEmps:
                ls.append(i.id)
                print(i.id,"post")

            daily_reports =  DailyReport.objects.filter(emp_id__in=ls)  #getting all the reports of employees that belong to a single leader
            
            if  (party != "" or  emp !="" or workdate !=""):
                if (party != ""):
                    daily_reports = daily_reports.filter(party=party).order_by('-workdate')
                elif(emp != ""):
                    daily_reports = daily_reports.filter(emp=emp).order_by('-workdate')
                elif(workdate !=""):
                    daily_reports =  daily_reports.filter(created_at__gte=datetime.date (2022,1, 1), created_at__lte=datetime.date (year, month, date)).order_by('-workdate')
            if(party != "" and  emp !="" and workdate != ""):
                daily_reports = daily_reports.filter(emp=emp,party=party,
                created_at__gte=datetime.date (2022,1, 1), created_at__lte=datetime.date (year, month, date)).order_by('-workdate')
                    
        
                # daily_reports = daily_reports.filter(party=party,emp=emp) 
              
        else:

            for i in subEmps:
                ls.append(i.id)
                print(i.id)

            daily_reports =  DailyReport.objects.filter(emp_id__in=ls).order_by('-workdate')
            
        context = {
                "daily_reports":daily_reports,
                "emps":subEmps,
                "partys":partys,
            }
        return render(request,"sub_daily_report.html",context)
    else:
        return HttpResponse("<center><h2>Cant Access this page Coz you are not a leader!!</center></h2>".upper())

@login_required
def sub_daily_report_approve(request,id):
    emp = Emp.objects.get(name = request.user.first_name)

    if Leaders.objects.filter(leaderid = emp.id).exists():
        if DailyReport.objects.filter(pk=id).exists():
            report = DailyReport.objects.get(pk=id)
            report.approved = True
            report.save()
            return redirect("sub_daily_report")
        else:
            return HttpResponse("Sorry the selected report is not present")
    else:
        return HttpResponse("Cant Access this page Coz you are not a leader!!".upper())