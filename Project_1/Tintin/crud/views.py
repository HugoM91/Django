from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
# Create your views here.

def index(request):
    return render(request, 'default_layout.html')


class CRUD(TemplateView):
    template_name = 'crud/display.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection'
        return context

class RegistoListView(ListView):
    template_name = 'crud/display.html'
    context_object_name = 'registo_lists'
    model = models.Registo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection'
        return context

class RegistoDetailView(DetailView):
    context_object_name = 'registo_detail'
    model = models.Registo
    template_name = 'crud/display.html'

class RegistoCreateView(CreateView):
    fields = ('username','password','usertype')
    model = models.Registo
