from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^polls2/poemlist2', views.poemlist2, name='poemlist2'),
]