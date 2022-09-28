
from django.db import models
from admin_panel.models import Party
from employee.models import Emp
# Create your models here.

class DailyReport(models.Model):
    emp = models.ForeignKey(Emp, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=False, auto_now_add=True,null=True)
    workdate = models.DateTimeField( auto_now=False, auto_now_add=True)
    work_detail = models.CharField( max_length=100) 
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.emp.name

