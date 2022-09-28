import re
from django.http import HttpResponse
from django.shortcuts import redirect, render ,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from employee.models import Emp
from django.contrib import messages

# Create your views here.



def loginn(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        
        if user is not None and user.is_staff:
            login(request,user)
            return redirect("index")
        elif user is not None:
            login(request,user)
            return redirect("emp_dash")
            
        else:
            return HttpResponse("Wrong Credentials..")
    return render(request,"login.html")




def emp_change_password(request):

    if request.method == "POST":
        emp = Emp.objects.get(name = request.user.first_name)
        
        password = request.POST['confirm']
        currrent_user = User.objects.get(username__exact = emp.mobile)
        currrent_user.set_password(password)
        currrent_user.save()
        print(currrent_user)
        # HttpResponse("Your Password has been updated!!!")
        messages.success(request,"Your Password has been changed successfully!")
        user = authenticate(username = emp.mobile,password = password)
        login(request,user)
        return redirect("emp_change_password")

    return render(request,"emp_change_password.html")



def logout(request):
    logout(request)
    return HttpResponseRedirect('login')    
    