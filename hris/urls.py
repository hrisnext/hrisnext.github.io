from django.urls import path

from . import views

app_name = 'hris'

urlpatterns = [
    path('', views.employee_list, name='employee'),
    path('add/', views.add_view, name='add'),
]
