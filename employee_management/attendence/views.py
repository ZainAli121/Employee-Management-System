from django.shortcuts import render
from .models import *
# Create your views here.

def attendence(request):
    attendences = Attendence.objects.all()
    for attendence in attendences:
        attendence.work_hours = attendence.calculate_work_hours()
    context = {'attendences' : attendences}
    return render(request, 'attendence/attendenceList.html', context)