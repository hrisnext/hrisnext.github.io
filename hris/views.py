from django.shortcuts import render

# Create your views here.
from hris.models import Employee

def index(request):
    latest_employees_list = Employee.objects.all()
    context = {
        'latest_employees_list' : latest_employees_list ,
    }
    return render(request, 'index.html', context=context)