from django.urls import path

from . import views

app_name = 'hris'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_employee, name='add'),
    path('employee/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employee/create/', views.EmployeeCreate.as_view(), name='employee-add'),
    path('employee/<int:pk>/',views.EmployeeDetailView.as_view(), name = 'employee-detail'),
    path('employee/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='employee-delete'),
    
    #path('add/', views.add_view, name='add'),
]
