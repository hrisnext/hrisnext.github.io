import datetime
from django import forms
from hris.models import Employee


class EmployeeForm(forms.ModelForm):
    '''

    '''
    class Meta:
        model = Employee
        fields = ('last_name','first_name', 'birthdate','sin_number','salary','employee_number','hire_date')
        
