from django.shortcuts import render, redirect
from .models import *
from employee_info.models import *
from users.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def apply_leave(request):
    if request.method == 'POST':
        user = request.user
        employee = request.user.employee
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        days_count = request.POST.get('days_count')
        leave_type = request.POST.get('leave_type')

        leave = Leave(employee=employee, start_date=start_date, end_date=end_date, days_count=days_count, leave_type=leave_type)
        if user.is_employee:
            leave.save()
            return redirect('employees_site')
        else:
            return render(request, 'users/login.html')

    leave_types = Leave.CHOICES
    context = {'leave_types': leave_types}
    return render(request, 'leave_requests/leave_form.html', context)