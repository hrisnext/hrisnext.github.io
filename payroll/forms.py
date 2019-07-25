import datetime
from django import forms
from payroll.models import Paycal



class PaycalForm(forms.ModelForm):
    '''
    Form used to create a Payroll object. Uses the calculator to find out what the numbers
    should be.
    
    '''
    class Meta:
        model = Paycal
        fields = ('p_period',)
