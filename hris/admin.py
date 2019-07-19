from django.contrib import admin
from hris.models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birthdate', 'sin_number','salary','employee_number','hire_date')
    #list_filter = ('status', 'due_back')
   