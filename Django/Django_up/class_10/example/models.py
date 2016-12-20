from django.db import models

# Create your models here.

class Poem(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "%s" % self.title
