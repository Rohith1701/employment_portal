# from django.shortcuts import render
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from .models import JobPost
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView, FormView)


class JobPostView(ListView):
    model = JobPost
    template_name = "jobpost/jobpost_list.html"


class JobLoginView(LoginView):
    template_name = "jobpost/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('Jobposts')

    def get_success_url(self):
        return reverse_lazy('Jobposts')


class RegisterPage(FormView):
    template_name = "jobpost/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


class JobList(LoginRequiredMixin, ListView):
    model = JobPost
    context_object_name = 'Jobposts'
    template_name = "jobpost/jobpost_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Jobposts'] = context['Jobposts'].filter(
            user=self.request.user)
        print(dir(context['Jobposts']))
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['Jobposts'] = context['Jobposts'].filter(
                title__startswith=search_input)
        context['search_input'] = search_input
        return context


class Jobdetail(LoginRequiredMixin, DetailView):
    model = JobPost
    context_object_name = 'Jobpost'
    template_name = "base/JobPost.html"


class JobCreate(LoginRequiredMixin, CreateView):

    model = JobPost
    fields = ['jobname', 'companyname', 'email', 'mobile', 'city', 'salery', ]
    success_url = reverse_lazy('Jobposts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobCreate, self).form_valid(form)


class JobUpdate(LoginRequiredMixin, UpdateView):
    model = JobPost
    fields = ['jobname', 'companyname', 'email', 'mobile', 'city', 'salery',]
    success_url = reverse_lazy('Jobposts')


class JobDelete(LoginRequiredMixin, DeleteView):
    model = JobPost
    context_object_name = 'JobPost'
    success_url = reverse_lazy('Jobposts')
    template_name = "jobpost/jobpost_delete.html"
