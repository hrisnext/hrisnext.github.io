import datetime
from django import forms
from django.forms import ModelForm

from timecards.models import Allcards

class AllcardsForm(forms.Form):
    '''
    Form used to create a Payroll object. Uses the calculator to find out what the numbers
    should be.
    
    '''
    class Meta:
        model = Allcards
        fields = ('employee_number','clocked_in','clocked_out')
'''
        widgets = {
            'clocked_in': forms.DateTimeInput(),
            'clocked_out': forms.DateTimeInput()
        }
class Signup(CreateView):
    form_class = AllcardsForm
    model = Allcards
'''