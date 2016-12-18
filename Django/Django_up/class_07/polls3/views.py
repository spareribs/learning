from django.shortcuts import render

from .models import Poem


# Create your views here.
def poemlist3(request):
    return render(request, 'poemlist3.html', {"show_title": "所有诗词信息", "poems": Poem.objects.all()})
