from django.shortcuts import render
from .models import *
from attendence.models import *
from leave_requests.models import *
from performance_evaluations.models import *
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
    
@login_required(login_url='login')
def employees_site(request):
    user = request.user
    if user.is_employee and not user.is_admin:
        employee = Employee.objects.get(user=user)
        # calculate the total number of sick leaves
        sick_leaves = Leave.objects.filter(employee=employee, leave_type='Sick Leave')
        sick_leave_count = 0
        for sick_leave in sick_leaves:
            if sick_leave.status == 'Approved':
                sick_leave_count += sick_leave.days_count

        # calculate the total number of casual leaves
        casual_leaves = Leave.objects.filter(employee=employee, leave_type='Casual Leave')
        casual_leave_count = 0
        for casual_leave in casual_leaves:
            if casual_leave.status == 'Approved':
                casual_leave_count += casual_leave.days_count

        # calculate earned leaves
        earned_leaves = Leave.objects.filter(employee=employee, leave_type='Earned Leave')
        earned_leave_count = 0
        for earned_leave in earned_leaves:
            if earned_leave.status == 'Approved':
                earned_leave_count += earned_leave.days_count

        # adjusted leave
        adjusted_leaves = Leave.objects.filter(employee=employee, leave_type='Adjusted Leave')
        adjusted_leave_count = 0
        for adjusted_leave in adjusted_leaves:
            if adjusted_leave.status == 'Approved':
                adjusted_leave_count += adjusted_leave.days_count

        # unpaid leave
        unpaid_leaves = Leave.objects.filter(employee=employee, leave_type='Unpaid Leave')
        unpaid_leave_count = 0
        for unpaid_leave in unpaid_leaves:
            if unpaid_leave.status == 'Approved':
                unpaid_leave_count += unpaid_leave.days_count

        # half day leave
        half_day_leaves = Leave.objects.filter(employee=employee, leave_type='Half-day Leave')
        half_day_leave_count = 0
        for half_day_leave in half_day_leaves:
            if half_day_leave.status == 'Approved':
                half_day_leave_count += half_day_leave.days_count
        
        context = {'employee' : employee, 'sick_leave_count' : sick_leave_count, 'casual_leave_count' : casual_leave_count, 'earned_leave_count' : earned_leave_count, 'adjusted_leave_count' : adjusted_leave_count, 'unpaid_leave_count' : unpaid_leave_count, 'half_day_leave_count' : half_day_leave_count}
        return render(request, 'employee_info/employeesPage.html', context)
    else:
        return render(request, 'users/login.html')
    
@login_required(login_url='login')
def employeeProfile(request, pk):
    user = request.user
    if user.is_employee:
        employee = Employee.objects.get(id=pk)
        performances = PerformanceEvaluation.objects.filter(employee=employee)
        context = {'employee' : employee, 'performances' : performances}
        return render(request, 'employee_info/employeeProfile.html', context)  
    
    else:
        return render(request, 'users/login.html') 