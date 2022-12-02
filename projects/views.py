from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView,UpdateView
from . import models, forms
from django.urls import reverse_lazy

# Create your views here.
class ProjectListView(ListView):
    model = models.Project
    template_name = 'project/list.html'
    
class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')