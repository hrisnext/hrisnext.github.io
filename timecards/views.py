from django.shortcuts import render
from django.views import generic
# Create your views here.

from timecards.models import Allcards

class AllcardsListView(generic.ListView):
    model = Allcards

class AllcardsDetailView(generic.DetailView):
    model = Allcards
