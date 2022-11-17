from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from . import forms
from . import models

# Create your views here.

@login_required
def home(request):
    return render(request=request, template_name="app1/home.html")

class MyModelDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    template_name = 'app1/my_model_detail.html'
    model = models.MyModel
    raise_exception = False

    def test_func(self):
        my_model:models.MyModel = self.get_object()
        return my_model.owner == self.request.user
        
class MyModelListView(LoginRequiredMixin, generic.ListView):
    template_name = 'app1/my_model_list.html'
    model = models.MyModel

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user.id)

class MyModelCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'app1/my_model_form.html'
    model = models.MyModel
    form_class = forms.MyForm
    success_url = reverse_lazy('app1:my_model_list')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MyModelUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    template_name = 'app1/my_model_form.html'
    model = models.MyModel
    form_class = forms.MyForm
    success_url = reverse_lazy('app1:my_model_list')

    def test_func(self):
        my_model:models.MyModel = self.get_object()
        return my_model.owner == self.request.user

class MyModelDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    template_name = 'app1/my_model_delete.html'
    model = models.MyModel
    success_url = reverse_lazy('app1:my_model_list')

    def test_func(self):
        my_model:models.MyModel = self.get_object()
        return my_model.owner == self.request.user
    