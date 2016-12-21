from django.db import models

# Create your models here.

class Poem(models.Model):
    owner = models.ForeignKey('auth.User', related_name='poems')

    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    type = models.IntegerField(default=0)

    def __str__(self):
        return self.title
