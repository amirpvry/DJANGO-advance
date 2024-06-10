from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm
from accounts.models import Profile

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todoapp/task_list.html'
    
    def get_queryset(self):
        profile = get_object_or_404(Profile, user=self.request.user)
        return Task.objects.filter(user=profile)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todoapp/task_form.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        profile = get_object_or_404(Profile, user=self.request.user)
        form.instance.user = profile
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todoapp/task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'todoapp/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
