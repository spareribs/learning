from django.db import models

# Create your models here.

class Task(models.Model):
    task_id = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Poem(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
