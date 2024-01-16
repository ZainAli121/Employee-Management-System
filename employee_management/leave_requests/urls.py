from . import views
from django.urls import path

urlpatterns = [
    path('', views.apply_leave, name='apply_leave'),
]