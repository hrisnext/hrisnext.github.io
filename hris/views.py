from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
from hris.models import Employee
from hris.forms import EmployeeForm

@login_required(login_url='/accounts/login')
def index(request):
    latest_employees_list = Employee.objects.all()
    context = {
        'latest_employees_list' : latest_employees_list ,
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




