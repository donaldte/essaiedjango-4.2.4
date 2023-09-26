from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from tache.forms import TacheFrom
# Create your views here.

from .models import Tache

class TacheListView(ListView):
    """
    Name: TacheListView
    Description: View definition for TacheListView.
    Author: donald 
    """
        
    model = Tache
    template_name = "tache_list.html"
    context_object_name = "taches"
    
    def get_queryset(self):
        return Tache.objects.all().order_by('-date_creation')


class TacheDetailView(DetailView):
    """
    Name: TacheDetailView
    Description: View definition for TacheDetailView.
    """
    
    model = Tache
    template_name = "tache_detail.html"
    context_object_name = "tache"    
    
    
    
class TacheModifyView(UpdateView):
    """
    Name: TacheModifyView
    Description: View definition for TacheModifyView.
    """
    #form_class = TacheFrom
    
    model = Tache
    template_name = "tache_modifier.html"
    fields = ['nom', 'description',  'fait']
    
    def get_success_url(self):
        return reverse("tache:tache_detail", kwargs={"pk": self.object.pk})   
    