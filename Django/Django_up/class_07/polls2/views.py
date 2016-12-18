from django.shortcuts import render
from .models import Poem


# Create your views here.
def poemlist2(req):
    return render(req, 'poemlist2.html', {'poems': Poem.objects.all()})
