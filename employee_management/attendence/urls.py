from . import views
from django.urls import path

urlpatterns = [
    path('overview/', views.attendence_overview_admin, name='attendence_admin'),
    path('employee/', views.attendence_employee, name='attendence_employee'),
]