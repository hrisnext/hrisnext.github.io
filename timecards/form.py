import datetime
from django import forms



class PayrollForm(forms.Form):
    '''
    Form used to create a Payroll object. Uses the calculator to find out what the numbers
    should be.
    
    '''
    