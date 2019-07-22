from django.db import models
from django.urls import reverse

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50, help_text='Enter employee\'s first name')
    last_name = models.CharField(max_length=50, help_text='Enter employee\'s last name')
    birthdate = models.DateField()
    sin_number = models.IntegerField()
    salary = models.DecimalField(max_digits = 16, decimal_places = 5)
    employee_number = models.IntegerField()
    hire_date = models.DateField()
    street_no = models.CharField(max_length=10, help_text='Enter employee\'s address')
    street_name = models.CharField(max_length=50, help_text='Enter employee\'s address')
    city = models.CharField(max_length=50, help_text='Enter employee\'s address')
    post_code = models.CharField(max_length=7, help_text='Enter employee\'s postal code')
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def get_absolute_url(self):
        return reverse('employee-detail', args=[str(self.id)])

    class Meta:
        ordering = ['last_name', 'first_name','birthdate']
    