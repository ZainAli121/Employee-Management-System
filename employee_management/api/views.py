from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/employees/',
        'api/employees/<str:pk>/',
        'api/attendence/',
        'api/attendence/<str:pk>/',
    ]
    return Response(routes)

@api_view(['GET'])
def getEmployees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getAttList(request):
    att = Attendence.objects.all()
    serializer = AttendenceSerializer(att, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAttEmp(request, pk):
    att = Attendence.objects.filter(employee=pk)
    serializer = AttendenceSerializer(att, many=True)
    return Response(serializer.data)