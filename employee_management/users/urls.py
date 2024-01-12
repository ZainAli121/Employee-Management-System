from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name='signup'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.loginUser, name='logout')
]