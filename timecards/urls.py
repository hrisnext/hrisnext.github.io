from django.urls import path

from . import views

app_name = 'timecards'

urlpatterns = [
    path('allcards/', views.AllcardsListView.as_view(), name='allcards-list'),
    path('allcardsdetail/<int:pk>', views.AllcardsDetailView.as_view(), name='allcards-detail'),
    path('allcards/create/', views.AllcardsCreate.as_view(), name='allcards_create'),
    path('allcards/<int:pk>/update/', views.AllcardsUpdate.as_view(), name='allcards_update'),
    path('allcards/<int:pk>/delete/', views.AllcardsDelete.as_view(), name='allcards_delete'),
    path('allcards/home', views.HomePageView.as_view(), name='home'),
]
