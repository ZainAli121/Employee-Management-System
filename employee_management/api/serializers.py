from employee_info.models import *
from attendence.models import *
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = '__all__'