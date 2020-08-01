from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django import forms
from django.views.generic.base import TemplateView


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
    
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['clocked_in'].widget = forms.DateTimeInput()
        form.fields['clocked_out'].widget = forms.DateTimeInput()
        return form
    

class AllcardsUpdate(LoginRequiredMixin, UpdateView):
    model = Allcards
    fields = ('employee_number','clocked_in','clocked_out')

class AllcardsDelete(LoginRequiredMixin, DeleteView):
    model = Allcards
    success_url = reverse_lazy('allcards-list')

class HomePageView(TemplateView):

    template_name = "timecards/allcards_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_timecards'] = Allcards.objects.all()[:5]
        return context