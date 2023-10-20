from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView, 
    DetailView, 
    UpdateView, 
    CreateView, 
    DeleteView
)
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from .models import Cours
from .forms import CoursForm

from compte.permissions import group_required, role_required, GroupRequiredMixin, RoleRequiredMixin
# class based view 

from django.views import View 

class CoursViewMixin(object):
    model = Cours 
    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = None 
        if pk is not None:
            obj = get_object_or_404(self.model, pk=pk)
        return obj


class FCourseListView(LoginRequiredMixin, RoleRequiredMixin,  View):
    
   
    
    roles = ['is_professor']
    
    template_name = 'cours/cours_lis.html'
    def get(self, request,  *args, **kwargs):
        queryset = Cours.objects.all()
        context = {
            'object_list': queryset
        }
        return render(request, self.template_name, context)

class FCoursDetailView(CoursViewMixin, View):
    template_name = 'cours/cours_detail.html'
    
    def get(self, request, pk=None, *args, **kwargs):
        context = {
           'object': self.get_object()
         }
        return render(request, self.template_name, context)
    
    def post(self, request):
        pass 
    

class FCourseCreateView(View):
    template_name = 'cours/cours_create.html'
    form = CoursForm()
    context = {
            'form': form
        }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    
    
    def post(self, request, *args, **kwargs):
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cours:cours-list')
        return render(request, self.template_name, self.context)
    
    
class FCourseUpdateView(CoursViewMixin, View):
    template_name='cours/cours_update.html'
    
    def get(self, request, pk=None, *args, **kwargs):
        context = {
            'form': CoursForm(instance=self.get_object())
        }
        return render(request, self.template_name, context) 
    
    
    def post(self, request, *args, **kwargs):
        form = CoursForm(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
            return redirect('cours:cours-list')
        return render(request, self.template_name, {'form': form})  
        

class FCourseDeleteView(CoursViewMixin, View):
    template_name = 'cours/cours_delete.html'   
    
    def get(self, request, pk=None, *args, **kwargs):
        context = {
            'object': self.get_object()
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            return redirect('cours:cours-list')
        return render(request, self.template_name, {'object': obj})
    
    
class CourseListView(ListView): # <modelname>_list.html
    template_name ='cours/cours_lis.html'
    queryset = Cours.objects.all()
    

class CourseDetailView(DetailView): # <modelname>_detail.html
    template_name ='cours/cours_detail.html'
    queryset = Cours.objects.all()    

class CourseCreateView(CreateView):
    form_class = CoursForm
    template_name = 'cours/cours_create.html'
    queryset = Cours.objects.all() 
    
    def form_valid(self, form):
        nom = form.cleaned_data.get('nom')
        if nom != "Francais":
            form.add_error("nom", "ce cours n'est pas autorisé validation vue")
            return self.form_invalid(form)
        return super().form_valid(form)
    

class CouseUpdateView(UpdateView):
    form_class = CoursForm
    template_name = 'cours/cours_update.html'
    queryset = Cours.objects.all()    
    

class CourseDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'cours.delete_cours'
    template_name = 'cours/cours_delete.html'
    queryset = Cours.objects.all() 
    
    
    def get_success_url(self):
        return reverse("cours:cours-list")

@role_required(['is_professor'])

@group_required('professor')
def list_view(request):
    queryset = Cours.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'cours/cours_lis.html', context)       