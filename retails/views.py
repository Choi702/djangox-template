from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Retail
from django.urls import reverse_lazy

# Create your views here.
    
class RetailListView(ListView):
    template_name = 'retail-list.html'
    model = Retail
    # fields = ['name', 'description', 'purchaser']

    
class RetailDetailView(DetailView):
    template_name = 'retail-detail.html'
    model = Retail

class RetailCreateView(CreateView):
    template_name = 'retail-create.html'
    model = Retail
    fields = ['name', 'description', 'purchaser']

class RetailUpdateView(UpdateView):
    template_name = 'retail-update.html'
    model = Retail
    fields = ['name', 'description', 'purchaser']
    
class RetailDeleteView(DeleteView):
    template_name = 'retail-delete.html'
    model = Retail
    success_url = reverse_lazy('retail_list')
    

