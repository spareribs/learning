from django.shortcuts import render
from polls.models import ToDo


# Create your views here.
def home(request):
    return render(request, 'home.html')


def todoList(request):
    return render(request, 'todoList.html', {"showType": "所有事件列表", "todoList": ToDo.objects.all().high().incomplete()})
