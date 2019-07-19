from django.urls import path

from . import views

app_name = 'timecards'

urlpatterns = [
    path('', views.timecards_list, name='timecards'),
    path('add/', views.add_view, name='add'),
]
