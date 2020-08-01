from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
import datetime
from django.http import HttpResponse


# Create your views here.
from hris.models import Employee
from hris.forms import EmployeeForm

'''

def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)

'''

@login_required(login_url='/accounts/login')
def index(request):
    latest_employees_list = Employee.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'latest_employees_list' : latest_employees_list ,
        'num_visits' : num_visits,
    }
    return render(request, 'hris/index.html', context=context)

class EmployeeListView(generic.ListView):
    model = Employee

class EmployeeDetailView(generic.DetailView):
    model = Employee



def add_employee(request):

    if request.method == 'POST':

        new_employee_form = EmployeeForm(data=request.POST)
        if  new_employee_form.is_valid():
                new_employee = new_employee_form.save()
    else:
        new_employee_form = EmployeeForm()

    return render(request,'hris/add.html',{'new_employee_form':new_employee_form,})

class EmployeeCreate(LoginRequiredMixin, CreateView):
    model = Employee
    fields = ('last_name','first_name', 'birthdate','sin_number','salary','employee_number','hire_date')

class EmployeeDelete(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = reverse_lazy('employee-list')

class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = ('last_name','first_name', 'birthdate','sin_number','salary','employee_number','hire_date')

'''
async def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.</body></html>' % now
    return HttpResponse(html)

'''