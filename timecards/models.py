from django.db import models
from hris.models import Employee
import datetime


# Create your models here.
class Allcards(models.Model):
    employee_number = models.ForeignKey('hris.Employee',on_delete=models.CASCADE)
    clocked_in = models.DateTimeField()
    clocked_out = models.DateTimeField()

    def worked_day():
        pass
    def worked_hours():
        pass
    def __str__(self):
        return self.employee_number + "worked %s on %s" %(self.worked_day, self.worked_hours) 