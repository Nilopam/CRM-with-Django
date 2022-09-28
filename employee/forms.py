import imp
from django import forms

from .models import *

# class LoginForm(forms.Form):
#     UserID = forms.CharField( max_length=20, required=True)
#     Password = forms.CharField(widget=forms.PasswordInput,max_length=20, required=True)


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super(NoticeForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'




class EmpForm(forms.ModelForm):
    
    class Meta:
        model = Emp
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'joining_Date': forms.DateInput(attrs={'type': 'date'}),
            # 'field_y': Forms.Select(attrs{'class': 'myclass'}),
        }

    def __init__(self,*args,**kwargs):
        super(EmpForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

# class EmpOfficeForm(forms.ModelForm):
    
#     class Meta:
#         model = EmpOffice
#         fields = '__all__'

#     def __init__(self,*args,**kwargs):
#         super(EmpOfficeForm,self).__init__(*args,**kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'

# class EmpContactForm(forms.ModelForm):
    
#     class Meta:
#         model = EmpContact
#         fields = '__all__'

#     def __init__(self,*args,**kwargs):
#         super(EmpContactForm,self).__init__(*args,**kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'


# class EmpBankForm(forms.ModelForm):
    
#     class Meta:
#         model = EmpBank
#         fields = '__all__'

#     def __init__(self,*args,**kwargs):
#         super(EmpBankForm,self).__init__(*args,**kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'






# class EmpSalaryForm(forms.ModelForm):
    
#     class Meta:
#         model = EmpSalary
#         fields = '__all__'

#     def __init__(self,*args,**kwargs):
#         super(EmpSalaryForm,self).__init__(*args,**kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'





# class EmpDocForm(forms.ModelForm):
    
#     class Meta:
#         model = EmpDoc
#         fields = '__all__'

#     def __init__(self,*args,**kwargs):
#         super(EmpDocForm,self).__init__(*args,**kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'

