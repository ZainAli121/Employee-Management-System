from . import views
from django.urls import path

urlpatterns = [
    path('/overview/', views.attendence, name='attendence'),
]