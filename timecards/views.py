from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


from timecards.models import Allcards
from timecards.forms import AllcardsForm

class AllcardsListView(generic.ListView):
    model = Allcards

class AllcardsDetailView(generic.DetailView):
    model = Allcards

class AllcardsCreate(LoginRequiredMixin, CreateView):
    model = Allcards
    fields = ('employee_number','clocked_in','clocked_out')

class AllcardsUpdate(LoginRequiredMixin, UpdateView):
    model = Allcards
    fields = ('employee_number','clocked_in','clocked_out')

class AllcardsDelete(LoginRequiredMixin, DeleteView):
    model = Allcards
    success_url = reverse_lazy('allcards-list')

