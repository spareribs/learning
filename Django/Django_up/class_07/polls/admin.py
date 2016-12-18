from django.contrib import admin
from polls.models import Poem, ToDo
# Register your models here.
admin.site.register(Poem)
admin.site.register(ToDo)
