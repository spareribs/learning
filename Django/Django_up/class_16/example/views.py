from django.shortcuts import render
from . import signals
from .models import Poem, Task
# Create your views here.

def index(request):
    signals.signalAllen.send(sender=None, allen='test')
    return render(request, template_name='index.html')

def disconnect_signal(request):
    signals.signalAllen.disconnect(signals.signal_callback)
    return render(request, template_name='index.html')

def modify(request):
    poem = Poem.objects.get(pk=1)
    poem.title = '1'
    # 会发送两个信号pre_save和post_save
    poem.save()

    task = Task.objects.get(pk=1)
    task.name = '1'
    task.save()

    return render(request, template_name='index.html')