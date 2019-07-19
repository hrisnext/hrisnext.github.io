from django.db import models
from django.urls import reverse

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50, help_text='Enter employee\'s first name')
    last_name = models.CharField(max_length=50, help_text='Enter employee\'s last name')
    birthdate = models.DateField()
    sin_number = models.IntegerField()
    salary = models.IntegerField()
    employee_number = models.IntegerField()
    hire_date = models.DateField()

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def get_absolute_url(self):
        return reverse('employee-detail', args=[str(self.id)])

    class Meta:
        ordering = ['last_name', 'first_name','birthdate']
    