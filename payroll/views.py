from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView


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
    fields = ('p_period',)

class PaycalUpdate(LoginRequiredMixin, UpdateView):
    model = Paycal
    fields = ('p_period',)

class PaycalDelete(LoginRequiredMixin, DeleteView):
    model = Paycal
    success_url = reverse_lazy('paycal-list')