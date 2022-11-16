from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from . import forms
from . import models

# Create your views here.

@login_required
def home(request):
    return render(request=request, template_name="app1/home.html")

class MyModelDetailView(generic.DetailView):
    template_name = 'app1/my_model_detail.html'
    model = models.MyModel


class MyModelListView(generic.ListView):
    template_name = 'app1/my_model_list.html'
    model = models.MyModel


class MyModelCreateView(generic.CreateView):
    template_name = 'app1/my_model_form.html'
    model = models.MyModel
    form_class = forms.MyForm
    success_url = reverse_lazy('app1:my_model_list')

class MyModelUpdateView(generic.UpdateView):
    template_name = 'app1/my_model_form.html'
    model = models.MyModel
    form_class = forms.MyForm
    success_url = reverse_lazy('app1:my_model_list')

class MyModelDeleteView(generic.DeleteView):
    template_name = 'app1/my_model_delete.html'
    model = models.MyModel
    success_url = reverse_lazy('app1:my_model_list')