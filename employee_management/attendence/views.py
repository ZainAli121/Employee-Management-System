from django.shortcuts import render
from .models import *
from attendence.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def attendence_overview_admin(request):
    page = 'admin'
    attendences = Attendence.objects.all()
    for attendence in attendences:
        attendence.work_hours = attendence.calculate_work_hours()
    context = {'attendences' : attendences, 'page' : page}
    return render(request, 'attendence/attendenceList.html', context)

@login_required(login_url='login')
def attendence_employee(request):
    employee = Employee.objects.get(user=request.user)
    attendences = Attendence.objects.filter(employee=employee)
    for attendence in attendences:
        attendence.work_hours = attendence.calculate_work_hours()
    context = {'attendences' : attendences}
    return render(request, 'attendence/attendenceList.html', context)

