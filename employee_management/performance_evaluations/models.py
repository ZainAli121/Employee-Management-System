from django.db import models
from employee_info.models import *

# Create your models here.
class PerformanceEvaluation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    rating = models.IntegerField()
    comments = models.TextField()
    
    def __str__(self):
        return self.employee.first_name+  "  " + self.comments
