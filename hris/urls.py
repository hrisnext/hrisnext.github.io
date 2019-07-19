from django.urls import path

from . import views

app_name = 'hris'

urlpatterns = [
    path('', views.index, name='index'),
    path('employee/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employee/<int:pk>',views.EmployeeDetailView.as_view(), name = 'employee-detail'),
    #path('add/', views.add_view, name='add'),
]
