from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.template import  RequestContext, Template,loader
from django.http import HttpResponse
from .rates import qcrates 
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

class PaycalCreate(LoginRequiredMixin, CreateView):
    model = Paycal
    fields = '__all__'

class PaycalUpdate(LoginRequiredMixin, UpdateView):
    model = Paycal
    fields = '__all__'

class PaycalDelete(LoginRequiredMixin, DeleteView):
    model = Paycal
    success_url = reverse_lazy('paycal-list')

def simulation(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        rate = request.POST.get('rate')
        hours = request.POST.get('hours')
        payf = request.POST.get('payf')
        wage = float(rate)*float(hours)
        wcb = round(float(wage*float(qcrates.wcb_er_rate)),2)
        cpp = round(float(wage*float(qcrates.cpp_ee_rate)),2)
        ei = round(float(wage*float(qcrates.ei_ee_rate)),2)
        qpip = round(float(wage*float(qcrates.qpip_ee_rate)),2)
        #adding the values in a context variable
        context = {
            'rate': rate,
            'hours': hours,
            'qpip': qpip,
            'wcb': wcb,
            'cpp': cpp,
            'ei':ei,
            'qpip':qpip,
        }

        #getting our showdata template

        #returing the template
        return render(request,'payroll/showsimulation.html',context)
    else:
        #if post request is not true
        #returing the form template
        return render(request,'payroll/simulation.html')
