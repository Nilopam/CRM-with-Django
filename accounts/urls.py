from django.urls import path, include
from . import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [
  
  
    
    
    path('emp_change_password/', user_view.emp_change_password, name ='emp_change_password'),

    # path('adminlogin/', user_view.loginn, name ='login'),
    path('login/', user_view.loginn, name ='login'),
    path('', user_view.loginn, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    
  
]