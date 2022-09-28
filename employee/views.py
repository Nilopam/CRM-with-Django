
from django.contrib import messages
import random
import string

from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from admin_panel.models import *
from .forms import *
# Create your views here.

def create_emp(request):
    if request.user.is_staff:
        if request.method == "POST":
            print("got post request")
            Empform = EmpForm(request.POST)
            smobile = request.POST['mobile']
            empname = request.POST['name']
            empemail = request.POST['email']
            
            print("checking form is valid or not")
            if Empform.is_valid():
                print("checking mobile numebr is present or not")
                if not User.objects.filter(username=smobile).exists():
                    print("trying to  save emp information")
                     
                    Empform.save()
                    print("saved succcessfully")
                else:
                    return HttpResponse("Mobile number is already registered".upper())

                if Emp.objects.filter(name = empname).exists():

                    emp = Emp.objects.get(name = empname)
                    print("checking leader or not")
                    if emp.emp_type == "leader":
                        lead = Leaders(leadername = emp.name,leaderid=emp.id)
                        lead.save()
                    
                        
                else:
                    return HttpResponse(f"{empname}-emp not exists")


                
                # creating user and pass for emp with random passsof alphanum
                password = ''.join(random.choices(string.ascii_uppercase+string.digits,k=6))
                with open("emp_pass.txt", "a") as f:
                    f.write(f"{empname} ::::::: {password}\n")
                myuser = User.objects.create_user(username=smobile,password=password)
                myuser.first_name = empname
                myuser.email = empemail
                myuser.save()

                return redirect("show_emp")
            else:
                return HttpResponse(f"<body>{Empform.errors}</body>")

        Empform = EmpForm()
        return render(request,"emp_crud/create_emp.html",{"Empform":Empform})
    else:
        return redirect("login")
    
    
    
        # if request.method == "POST":
        #     Empform = EmpForm(request.POST, request.FILES)
        #     smobile = request.POST['mobile']
        #     empname = request.POST['name']
        #     empemail = request.POST['email']
        #     if Empform.is_valid():
                
        #         Empform.save()
                
        #         if Emp.objects.get(name = empname):
        #             emp = Emp.objects.get(name = empname)
        #             if emp.emp_type == "leader":
        #                 lead = Leaders(leadername = emp.name,leaderid=emp.id)
        #                 lead.save()
        #             else:
        #                 return HttpResponse(f"{empname}-emp is not leader")
        #         else:
        #             return HttpResponse(f"{empname}-emp not exists")
                
        #         # creating user and pass for emp with random passsof alphanum
        #         password = ''.join(random.choices(string.ascii_uppercase+string.digits,k=6))
        #         with open("emp_pass.txt", "a") as f:
        #             f.write(f"{empname} ::::::: {password}")
        #         myuser = User.objects.create_user(username=smobile,password=password)
        #         myuser.first_name = empname
        #         myuser.email = empemail
        #         myuser.save()
        #         print("saved")
        #         return redirect("show_emp")
        #     else:
        #         return HttpResponse("Emp creation failed")
        # else:
        #     Empform = EmpForm()
        # return render(request,"emp_crud/create_emp.html",{"Empform":Empform})
    
    
    
    
    
    # if request.method == "POST":
    #     Empform = EmpForm(request.POST, request.FILES)
    #     if Empform.is_valid():
            
    #         empname = Empform.cleaned_data['name']
    #         smobile = Empform.cleaned_data['mobile']
    #         empemail = Empform.cleaned_data['email']

    #         Empform.save()

    #         if Emp.objects.get(name = empname):
    #             emp = Emp.objects.get(name = empname)
    #             if emp.emp_type == "leader":
    #                 lead = Leaders(leadername = emp.name,leaderid=emp.id)
    #                 lead.save()
    #             else:
    #                 return HttpResponse(f"{empname}-emp is not leader")
    #         else:
    #             return HttpResponse(f"{empname}-emp not exists")
    #         # creating user and pass for emp with random passsof alphanum
    #         password = ''.join(random.choices(string.ascii_uppercase+string.digits,k=6))
    #         with open("emp_pass.txt", "a") as f:
    #             f.write(f"{empname} ::::::: {password}")
    #         myuser = User.objects.create_user(username=smobile,password=password)
    #         myuser.first_name = empname
    #         myuser.email = empemail
    #         myuser.save()
    #         print("saved")
    #         return redirect("show_emp")

    # else:
    #     Empform = EmpForm()
    # return render(request,"emp_crud/create_emp.html",{"Empform":Empform})
    



def show_emp(request):
    if request.user.is_staff:
        employees = Emp.objects.all()
        return render(request,"emp_crud/show_emp.html",{"employees":employees})
    else:
        return redirect("login")
def update_emp(request,id):

    if request.user.is_staff:

        empid  = Emp.objects.get(pk=id)
        
        print(f"got update reqeust from- {empid.name},{empid.id}".upper())
        print(empid.mobile,empid.name)

        Empform = EmpForm(instance=empid)
        if request.method == "POST":
            print(f"Processing post request of updation for {empid}".upper())
            Empform = EmpForm(request.POST,request.FILES,instance=empid)
            # smobile = request.POST['mobile']
            # empname = request.POST['name']
            emp_type = request.POST['emp_type']
            print(f"Checking form data".upper())
            if Empform.is_valid():
                if User.objects.filter(username = empid.mobile).exists():

                    user =  User.objects.get(username = empid.mobile)

                    Empform.save()
                    print(f"Employee {empid} has been updated successfully".upper())
                    print(f"checking if Employee {empid} is leader or not".upper())

                    if emp_type == "employee" and Leaders.objects.filter(leaderid=id).exists():
                        print(f"Got normal employee request for {empid}".upper())
                        obj = Leaders.objects.get(leaderid = id)
                        print(f"changing permission rights!".upper())
                        obj.delete()
                        print("Removed From leaders grup".upper())
                    elif emp_type == "leader":
                        if not Leaders.objects.filter(leaderid=id).exists():
                            print(f"Got leader employee request for {empid}".upper())
                            obj = Emp.objects.get(id =id)
                            obj.under_of_id = None
                            obj.save()
                            print(f"{empid} is leader now".upper())
                    user.username = empid.mobile
                    user.first_name = empid.name
                    user.save()
                    
                    return redirect("show_emp")
                else:
                    return HttpResponse("User doesnt exists!")


        return render(request,"emp_crud/update_emp.html",{"Empform":Empform})
    else:
        return redirect("login")







def delete_emp(request, id):
    
    if request.user.is_staff:
        
        if Emp.objects.filter(pk=id).exists():

            emp = Emp.objects.get(pk=id)

            try:
                user = User.objects.get(username = emp.mobile)
            except Exception as e:
                print(e)
                print(f"selected emp is not present in users table-emp.id-{emp.id},{emp.name}".upper())
                return HttpResponse("Selected emp is not present in U")
                
            else:
                user.delete()
                print("user delted")
                ob = Leaders.objects.get(leaderid = emp.id)
                ob.delete()
                print(f"{emp.id},{emp.name}".upper())
                emp.delete()
                print("emp deleted")
                
            return redirect("show_emp")
        else :
            return HttpResponse(f"Employee Not exists".upper())


    else:
        return redirect("login")
# employee crud views ends





def payslip(request):
    

    if request.user.is_staff:
        return render(request, "employee/payslip.html")
    else:
        return redirect("login")


def attendance(request):
    
    if request.user.is_staff:
        attendances = Attendance.objects.all()
        return render(request, "attendance/attendance.html",{"attendances":attendances})
    else:
        return redirect("login")



def reject_attendance(request,id):
    
    if request.user.is_staff:
        if Attendance.objects.filter(pk=id).exists():
            attendance = Attendance.objects.get(pk=id)
            if attendance.status == "A":
                attendance.status = "R"
                attendance.save()
                return redirect("attendance")
            if attendance.status == "R":
                return HttpResponse("Already Rejected")
        else:
            return HttpResponse("Not Present")
    else:
        return redirect("login")

def makefull(request,id):
    
    if request.user.is_staff:
        if Attendance.objects.filter(pk=id).exists():
            attendance = Attendance.objects.get(pk=id)
            if attendance.half:
                attendance.half = False
                attendance.save()
                return redirect("attendance")
            else:
                return HttpResponse("its already Full")
        else:
            return HttpResponse("Not Present")
    else:
        return redirect("login")

def makehalf(request,id):
    
    if request.user.is_staff:
        if Attendance.objects.filter(pk=id).exists():
            attendance = Attendance.objects.get(pk=id)
            if not attendance.half:
                attendance.half = True
                attendance.save()
                return redirect("attendance")
            else:
                return HttpResponse("its already Half")
        else:
            return HttpResponse("Not Present")
    else:
        return redirect("login")




def custom_attendance(request):
    
    if request.user.is_staff:
        emps = Emp.objects.all()
        if request.method == "POST":
            empid = request.POST["emp_name"]
            empdate = request.POST["emp_date"]
            # emp = Emp.objects.get(name = empid)
            if Emp.objects.filter(id = empid).exists():
                print(f"{empid} exists".upper())
                empid = Emp.objects.get(id = empid)
                print("getting instanace".upper())
                print(empid,empdate)
                if not Attendance.objects.filter(emp=empid,date = empdate).exists():
                    obj = Attendance(emp = empid,date = empdate)
                    obj.save()
                    messages.success(request,f"Custom Attendance Done for {empid} on {empdate}")
                    print(f"Custom Attendance Done for {empid} on {empdate}".upper())
                else:
                    return HttpResponse(f"<center><h2>{empid}'s attendane is already presented on this date {empdate}</h2></center>")
                
            else:
                return HttpResponse("emp is not present")
        else:
            emps = Emp.objects.all()
            

        return render(request,"attendance/custom_attendance.html",{"emps":emps})
    else:
        return redirect("login")




def payslip(request):
    
    if request.user.is_staff:
        payslips = Payslip.objects.all()
        return render(request,"payslip/payslip.html",{'payslips':payslips})
    else:
        return redirect("login")
    


def leave_approval(request):
    
    if request.user.is_staff:
        leaves = LeaveApproval.objects.all()
        return render(request, "leave_approval/leave_approval.html",{"leaves":leaves})
    else:
        return redirect("login")



def leave_approval_approve(request,id):
    
    if request.user.is_staff:
        if LeaveApproval.objects.get(pk=id):
            leave = LeaveApproval.objects.get(pk=id)
            if  leave.status == "R" or leave.status=="P":
                leave.status = "A"
                leave.save()
                return redirect("leave_approval")
            else:
                return HttpResponse("its already Aprooved")
        return HttpResponse("Not Present")
    else:
        return redirect("login")

    
    




def leave_approval_reject(request,id):
    
    if request.user.is_staff:
        if LeaveApproval.objects.get(pk=id):
            leave = LeaveApproval.objects.get(pk=id)
            if not leave.status == "R" or leave.status=="P":
                leave.status = "R"
                leave.save()
                return redirect("leave_approval")
            else:
                return HttpResponse("its already Rejected")
        return HttpResponse("Not Present")
    else:
        return redirect("login")





def notice(request):
    
    if request.user.is_staff:
        notices = Notice.objects.all()
        return render(request,"notice/notice.html",{'notices':notices})
    else:
        return redirect("login")


def notice_add(request):
    
    if request.user.is_staff:
        if request.method == "POST":
            form = NoticeForm(request.POST,request.FILES)
            if form.is_valid():
                # name = form.cleaned_data['name']
                # content = form.cleaned_data['notice_content']
                # attachment = form.cleaned_data['attachment']
                # notice= Notice(name=name,notice_content=content,attachment=attachment)
                # notice.save()
                form.save()
                return redirect("notice")
            else:
                HttpResponse("DATA input is not Valid")
        else:
            print("Got GET request from notice")
            form = NoticeForm()
        return render(request,"notice/notice_add.html",{"form":form})
    else:
        return redirect("login")


def notice_edit(request,id):
    
    if request.user.is_staff:
        notice  = Notice.objects.get(pk=id)
        form = NoticeForm(instance=notice)
        if request.method == "POST":
            form = NoticeForm(request.POST,request.FILES,instance=notice)
            if form.is_valid():
                form.save()
                return redirect("notice")
            
        return render(request,"notice/notice_edit.html",{'form':form})
    else:
        return redirect("login")


def notice_delete(request,id):
    
    if request.user.is_staff:
        notice  = Notice.objects.get(pk=id)
        notice.delete()
        return redirect('notice')
    else:
        return redirect("login")



def travel(request):
    
    if request.user.is_staff:
        transports = TravelAllow.objects.all()
        return render(request,"travel/travel.html",{'transports':transports})
    else:
        return redirect("login")





def travel_approve(request,id):
    
    if request.user.is_staff:
        if TravelAllow.objects.get(pk=id):
            leave = TravelAllow.objects.get(pk=id)
            if  leave.status == "R" or leave.status=="P":
                leave.status = "A"
                leave.save()
                return redirect("travel")
            else:
                return HttpResponse("its already Aprooved")
        return HttpResponse("Not Present")
    else:
        return redirect("login")


    
    




def travel_reject(request,id):
    
    if request.user.is_staff:
        if TravelAllow.objects.get(pk=id):
            leave = TravelAllow.objects.get(pk=id)
            if  leave.status == "A" or leave.status=="P":
                leave.status = "R"
                leave.save()
                return redirect("travel")
            else:
                return HttpResponse("its already Rejected")
        return HttpResponse("Not Present")
    else:
        return redirect("login")







def resignation(request):
    
    if request.user.is_staff:
        resignations = Resignation.objects.all()
        return render(request,"resignation/resignation.html",{'resignations':resignations})
    else:
        return redirect("login")



##########################
def resignation_approve(request,id):
    
    if request.user.is_staff:
        if Resignation.objects.get(pk=id):
            resignation = Resignation.objects.get(pk=id)
            if resignation.status == "P" or resignation.status == "R":
                resignation.status = "A"
                resignation.save()
                return redirect("resignation")
            elif resignation.status == "A":
                return HttpResponse("Already Approved!!")
            else:
                return HttpResponse("Something wrong in aprooval")
    
        return HttpResponse("Not Present")
    else:
        return redirect("login")



def resignation_reject(request,id):
    
    if request.user.is_staff:
        if Resignation.objects.get(pk=id):
            resignation = Resignation.objects.get(pk=id)
            if resignation.status == "P" or resignation.status == "A":
                resignation.status = "R"
                resignation.save()
                return redirect("resignation")
            elif resignation.status == "R":
                return HttpResponse("Already Rejected!!")
            else:
                return HttpResponse("Something wrong in aprooval")
    
        return HttpResponse("Not Present")
    else:
        return redirect("login")

