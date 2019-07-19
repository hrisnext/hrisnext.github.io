from django.shortcuts import render
from django.views import generic


# Create your views here.
from hris.models import Employee

def index(request):
    latest_employees_list = Employee.objects.all()
    context = {
        'latest_employees_list' : latest_employees_list ,
    }
    return render(request, 'index.html', context=context)

class EmployeeListView(generic.ListView):
    model = Employee

class EmployeeDetailView(generic.DetailView):
    model = Employee

