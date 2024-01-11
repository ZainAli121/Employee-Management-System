from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    GENDER_CHOICES = [
        ('M' , 'Male'),
        ('F' , 'Female'),
        ('O' , 'Other'),
    ]

    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True, unique=True)
    contact_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=2000, null=True)
    roll = models.CharField(max_length=2000, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
