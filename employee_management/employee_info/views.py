from django.shortcuts import render
from .models import *
from attendence.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def admin_employees_site(request):
    user = request.user
    if user.is_admin:
        # on-time employees
        att_count = 0
        attendences = Attendence.objects.all()
        for attendence in attendences:
            if attendence.status == 'Present':
                if attendence.time_in.hour <= 9:
                    att_count += 1

        # late employees
        late_count = 0
        for attendence in attendences:
            if attendence.status == 'Present':
                if attendence.time_in.hour > 9:
                    late_count += 1

        # early leave employees
        early_leave_count = 0
        for attendence in attendences:
            if attendence.status == 'Present':
                if attendence.time_out.hour < 17:
                    early_leave_count += 1

        # absent employees
        absent_count = 0
        for attendence in attendences:
            if attendence.status == 'Absent':
                absent_count += 1

        # time-off employees
        time_off_count = 0
        for attendence in attendences:
            if attendence.status == 'Time Off':
                time_off_count += 1

        employees = Employee.objects.all()

        context = {'employees' : employees, 'att_count' : att_count, 'late_count' : late_count, 'early_leave_count' :   early_leave_count, 'absent_count' : absent_count, 'time_off_count' : time_off_count}
        return render(request, 'employee_info/adminPage.html', context)
    
    else:
        return render(request, 'users/login.html')
    

def employees_site(request):
    user = request.user
    if user.is_employee:
        return render(request, 'employee_info/employeesPage.html')
    else:
        return render(request, 'users/login.html')