from django.shortcuts import render
from .models import *

# Create your views here.

def employees(request):
    employees = Employee.objects.all()
    context = {'employees' : employees}
    return render(request, 'employee_info/adminPage.html', context)