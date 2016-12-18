from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^polls3/poemlist3', views.poemlist3, name="poemlist3")
]