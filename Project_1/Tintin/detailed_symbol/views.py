from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models



# Create your views here.
def index(request):
    return render(request, 'default_layout.html')

def detailed_symbol(request):
    return render(request, 'detailed_symbol/display.html')


class CRUD(TemplateView):
    template_name = 'crud/display.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection'
        return context
