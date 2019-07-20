from django.db import models
from hris.models import Employee
import datetime
from django.utils.timezone import utc

# Create your models here.
class Allcards(models.Model):
    employee_number = models.ForeignKey('hris.Employee',on_delete=models.CASCADE)
    clocked_in = models.DateTimeField()
    clocked_out = models.DateTimeField()

    def worked_day():
        in_date = clocked_in.date()
        out_date = clocked_out.date()

        if in_date == out_date:
            return in_date
        else:
            return in_date , out_date

    def worked_hours():
        timediff = clocked_out - clocked_in 
        return timediff.total_seconds()
        
