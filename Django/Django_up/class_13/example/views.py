from django.shortcuts import render, HttpResponseRedirect
from .models import Task
from django.views.generic import TemplateView, ListView, View
from .forms import AddTaskForm


def index(request):
    return render(request, 'index.html')


class IndexView(TemplateView):
    template_name = 'index.html'


class ShowTasksView(ListView):
    template_name = 'tasks.html'
    model = Task


class DisplaySingleTaskView(TemplateView):
    template_name = 'single_task.html'

    def get_context_data(self, **kwargs):
        context = super(DisplaySingleTaskView, self).get_context_data(**kwargs)
        task_id = self.kwargs.get('task_id', 0)
        context['task'] = Task.objects.get(task_id=task_id)
        return context


class AddModelView(View):
    form_class = AddTaskForm
    template_name = 'add_task.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/success')
