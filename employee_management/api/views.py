from rest_framework.response import Response
from rest_framework.decorators import api_view

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