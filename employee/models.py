from django.db import models
from django.contrib.auth.models import User
from admin_panel.models import Designation,Place
# Create your models here.


class Leaders(models.Model):

    leadername = models.CharField(max_length=50)
    leaderid= models.IntegerField()

    def __str__(self):
        return self.leadername
    



class Emp(models.Model):
    empTypes=(
        ('leader','Team Leader'),
        ('employee','Normal Employee')
    )
    name = models.CharField( max_length=50,unique=True)
    address =models.CharField( max_length=50)
    dob = models.DateField()
    # empCode = models.CharField( max_length=50)
    guardian_name = models.CharField( max_length=50)
    
    qualification = models.CharField( max_length=50)

    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
    place_of_work =models.ForeignKey(Place,on_delete=models.CASCADE)
    joining_Date = models.DateField()
    emp_type = models.CharField(choices=empTypes, max_length=50)
    under_of = models.ForeignKey("leaders",default="", on_delete=models.CASCADE,null=True,blank=True)

    mobile = models.CharField( max_length=14,unique=True)
    corporate_mobile = models.CharField( max_length=14,blank=True,null=True)
    email = models.EmailField( max_length=254,unique=True)
    alternate_mobile =models.CharField( max_length=14,blank=True,null=True)


    
    ifsc_code = models.CharField( max_length=50,blank=True,null=True)
    bank_name = models.CharField( max_length=50,blank=True,null=True)
    branch_name = models.CharField( max_length=50,blank=True,null=True)
    account_number = models.CharField( max_length=50,blank=True,null=True)
    esi_number = models.CharField( max_length=50,blank=True,null=True)
    pan = models.CharField( max_length=50,blank=True,null=True)
    adhaar = models.CharField( max_length=50,blank=True,null=True)
    vote = models.CharField( max_length=50,blank=True,null=True)
    passport = models.CharField( max_length=50,blank=True,null=True)
    belonging = models.TextField( max_length=500,blank=True,null=True)

    gross_salary = models.CharField(max_length=50,blank=True,null=True)
    mobile_salary = models.CharField(max_length=50,blank=True,null=True)
    basic_salary = models.CharField(max_length=50,blank=True,null=True)
    house_salary = models.CharField(max_length=50,blank=True,null=True)
    education_salary = models.CharField(max_length=50,blank=True,null=True)
    medical_salary = models.CharField(max_length=50,blank=True,null=True)
    other_salary = models.CharField(max_length=50,blank=True,null=True)
    esi_emp = models.CharField(max_length=50,blank=True,null=True)
    esi_empr = models.CharField(max_length=50,blank=True,null=True)
    esi_total = models.CharField(max_length=50,blank=True,null=True)
    net_salary = models.CharField(max_length=50,blank=True,null=True)
    monthly_ctc = models.CharField(max_length=50,blank=True,null=True)
    yearly_ctc =models.CharField(max_length=50,blank=True,null=True)
    
    education_doc = models.FileField( upload_to="uploads/education/", max_length=100,blank=True,null=True)
    experience_doc = models.FileField( upload_to="uploads/experience/", max_length=100,blank=True,null=True)
    pay_slip_doc = models.FileField( upload_to="uploads/pay_slip/", max_length=100,blank=True,null=True)
    resignation_doc = models.FileField( upload_to="uploads/resignation/", max_length=100,blank=True,null=True)
    photograph_doc = models.ImageField( upload_to="uploads/photograph/", max_length=100,blank=True,null=True)
    poi_doc = models.FileField( upload_to="uploads/id_proof/", max_length=100,blank=True,null=True)      #proof of identiy
    poa_doc = models.FileField( upload_to="uploads/education/", max_length=100,blank=True,null=True)
    
    def __str__(self):
        return self.name
    










class TravelAllow(models.Model):

    Status = (
        ('A','Approve'),
        ('R','Reject'),
    )

    emp = models.ForeignKey("Emp", on_delete=models.CASCADE)
    date = models.DateField( auto_now=False, auto_now_add=False)
    from_where = models.CharField( max_length=50)
    destination = models.CharField( max_length=50)
    distance = models.CharField(max_length=50)
    expense = models.CharField(max_length=50)
    purpose = models.CharField(max_length=100)
    remarks = models.CharField(max_length=50)
    status = models.CharField(choices=Status,max_length=10,default="P")

    def __str__(self):
        return self.emp.name

    
class Notice(models.Model):

    name = models.CharField(max_length=50)
    notice_content = models.CharField(max_length=500)
    attachment = models.FileField(upload_to='Notice', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name



class Resignation(models.Model):

    Status = (
        ('A','Approve'),
        ('R','Reject'),
        ('P','Pending'),
    )

    emp = models.ForeignKey("Emp", on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    experience_letter =models.CharField( max_length=50,blank=True) 
    release_letter = models.CharField( max_length=50,blank=True)
    status = models.CharField(choices=Status,default="P", max_length=1)
    def __str__(self):
        return self.emp.name

   

class LeaveApproval(models.Model):

    
    Category = (
        ('EL','EL'),
        ('CL','CL'),
    )
    Status = (
        ('A','Approve'),
        ('R','Reject'),
        ('P','Pending'),
    )
    emp = models.ForeignKey("Emp", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    from_date = models.DateField(auto_now=False, auto_now_add=False)
    to_date = models.DateField( auto_now=False, auto_now_add=False)
    category = models.CharField(choices=Category, max_length=50)
    reason = models.CharField( max_length=200)
    status = models.CharField(choices=Status, default="P",max_length=50)
    
 

    def __str__(self):
        return self.emp.name

    

class Attendance(models.Model):
    Status = (
        ('A','Approve'),
        ('R','Reject'),
        
    )
    emp = models.ForeignKey("Emp", on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    in_time = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True,null=True)
    out_time = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True,null=True)
    
    status = models.CharField(choices=Status,default="A", max_length=50)
    half = models.BooleanField(default=False)
    

    def __str__(self):
        return self.emp.name

    

    

class Payslip(models.Model):

    emp = models.ForeignKey("Emp", on_delete=models.CASCADE)
    # salary = models.ForeignKey("EmpSalary", on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.emp.name

    