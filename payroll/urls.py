from django.urls import path

from . import views

app_name = 'payroll'

urlpatterns = [
    path('', views.index, name='index'),
    path('paycallist/', views.PaycalListView.as_view(), name='paycal-list'),
    path('paycaldetail/', views.PaycalDetailView.as_view(), name='paycal-detail'),
]
