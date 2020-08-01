from django.urls import path

from . import views

app_name = 'payroll'

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.add, name='add'),
    path('simulation/', views.simulation, name='simulation'),
    path('paycallist/', views.PaycalListView.as_view(), name='paycal-list'),
    path('paycaldetail/', views.PaycalDetailView.as_view(), name='paycal-detail'),
    path('paycal/create/', views.PaycalCreate.as_view(), name='paycal_create'),
    path('paycal/<int:pk>/update/', views.PaycalUpdate.as_view(), name='paycal_update'),
    path('paycal/<int:pk>/delete/', views.PaycalDelete.as_view(), name='paycal_delete'),
]
