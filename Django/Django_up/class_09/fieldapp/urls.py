from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^testlist/', views.testlist, name='testlist'),
    url(r'^addfile/', views.addfile, name='addfile'),
]