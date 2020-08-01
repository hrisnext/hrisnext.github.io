from django.db import models
from hris.models import Employee
import datetime
from django.utils.timezone import utc

# Create your models here.
class Allcards(models.Model):
    employee_number = models.ForeignKey('hris.Employee',on_delete=models.CASCADE)
    clocked_in = models.DateTimeField()
    clocked_out = models.DateTimeField()
    out_date = models.DateField(blank=True, null=True, default = '')
    in_date = models.DateField(blank=True, null=True, default = '')
    worked_hours = models.DecimalField(max_digits = 16, decimal_places = 5, default = '0')

    @property
    def get_in_date(self):
        if self.clocked_in:
            return self.clocked_in.date()
    
    @property
    def get_out_date(self):
        if self.clocked_out:
            return self.clocked_out.date()

    @property
    def get_worked_hours(self):
        timediff = self.clocked_out - self.clocked_in 

        return timediff.total_seconds()/3600
        
    def save(self, *args, **kwargs):
          self.in_date = self.get_in_date
          self.out_date = self.get_out_date
          self.worked_hours = self.get_worked_hours
          super(Allcards, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.employee_number) + "had worked for " + str(self.worked_hours) + "hours"