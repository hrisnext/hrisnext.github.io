from django.urls import path

from . import views

app_name = 'timecards'

urlpatterns = [
    path('allcards/', views.AllcardsListView.as_view(), name='allcards-list'),
    path('allcardsdetail/<int:pk>', views.AllcardsDetailView.as_view(), name='allcards-detail'),
]
