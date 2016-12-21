from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^poems/$', views.PoemListView.as_view(), name="poem_list"),
    url(r'^poem/(?P<pk>[0-9]+)$', views.poem_detail, name="poem_list"),
]
