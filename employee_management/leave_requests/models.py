from django.db import models
from employee_info.models import Employee
# Create your models here.
class Leave(models.Model):

    CHOICES = [
        ('Casual Leave', 'Casual Leave'),
        ('Sick Leave', 'Sick Leave'),
        ('Earned Leave', 'Earned Leave'),
        ('Adjusted Leave', 'Adjusted Leave'),
        ('Half-day Leave', 'Half-day Leave'),
        ('Unpaid Leave', 'Unpaid Leave'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    days_count = models.IntegerField(default=0)
    status = models.CharField(max_length=100, default='Pending', choices=STATUS_CHOICES)
    leave_type = models.CharField(max_length=100, choices=CHOICES)

    def __str__(self):
        return f"{self.employee}"