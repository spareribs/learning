from django.db import models

# Create your models here.
class Poem(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    poem_id = models.IntegerField(default=0)

    def __str__(self):
        return self.title

