from django.shortcuts import render
from polls.models import ToDo, Poem, Book2


# Create your views here.
def home(request):
    return render(request, 'home.html', {'poems': Poem.objects.all(), 'book2': Book2.objects.all()})


def todoList(request):
    return render(request, 'todoList.html', {"showType": "所有事件列表", "todoList": ToDo.objects.all().high().incomplete()})
