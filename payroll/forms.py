import datetime
from django import forms
from hris.models import Employee


class PaycalForm(forms.ModelForm):
    '''
    Form used to create a Payroll object. Uses the calculator to find out what the numbers
    should be.
    
    '''
    