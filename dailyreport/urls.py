from django.urls import path
from . import views


urlpatterns = [
    path("daily_report/",views.daily_report,name="daily_report"),
    path("daily_report_approve/<int:id>",views.daily_report_approve,name="daily_report_approve"),

]