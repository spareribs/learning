from django.db import models

# Create your models here.

class Poem(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Task(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
