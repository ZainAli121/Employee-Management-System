from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/employees/',
        'api/employees/<str:pk>/',
        'api/employees/create/',
        'api/employees/<str:pk>/update/',
        'api/employees/<str:pk>/delete/',
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