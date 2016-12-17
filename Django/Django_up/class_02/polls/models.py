# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Poem(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s" %(self.author, self.title)