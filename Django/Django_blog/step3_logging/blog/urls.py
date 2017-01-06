from django.conf.urls import url
from blog.views import index

urlpatterns = [
    url(r'^$', index, name='index'),

]
