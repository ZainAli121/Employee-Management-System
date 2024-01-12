from django.db import models
from django.contrib.auth.models import AbstractUser
from employee_info.models import Employee

# Create your models here.
class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    profile_pic = models.ImageField(blank=True, default='avatar.svg')

    def __str__(self):
        return f"{self.username}"
