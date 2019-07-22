from django.shortcuts import render
from django.views import generic
# Create your views here.

from payroll.models import Paycal
from payroll.forms import PaycalForm

def index(request):
    payroll_history = Paycal.objects.all()
    context = {
        'payroll_history' : payroll_history ,
    }
    return render(request, 'payroll/index.html', context=context)

class PaycalListView(generic.ListView):

    model = Paycal

class PaycalDetailView(generic.DetailView):
    
    model = Paycal
