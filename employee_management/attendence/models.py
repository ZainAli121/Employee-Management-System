from django.db import models
from employee_info.models import Employee

# Create your models here.
class Attendence(models.Model):
    CHOICES = (('Present', 'Present'), ('Absent', 'Absent'), ('Time Off', 'Time Off'))

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    time_in = models.DateTimeField()
    time_out = models.DateTimeField()
    status = models.CharField(max_length=10, choices=CHOICES)

    def calculate_work_hours(self):
        if self.time_in and self.time_out:
            work_hours = self.time_out - self.time_in
            return work_hours
        else:
            return None

    def __str__(self):
        return self.employee.first_name + " " + str(self.date)
