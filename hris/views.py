from django.shortcuts import render
from django.views import generic


# Create your views here.
from hris.models import Employee
from hris.forms import EmployeeForm

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

    return render(request,'add.html',{'new_employee':new_employee,'new_employee_form':new_employee_form,})


