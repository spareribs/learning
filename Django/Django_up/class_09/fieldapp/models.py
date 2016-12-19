from django.db import models
from .fields import ListFiled, ContextTypeRestrictedFileField
# Create your models here.

class ListTest(models.Model):
    labels = ListFiled()

    def __str__(self):
        return "%s " % self.labels

class AddPdfFileModel(models.Model):
    name = models.CharField(max_length=100)
    file = ContextTypeRestrictedFileField(content_type='application/pdf', max_upload_size=5242880, upload_to='pdf')

    def __str__(self):
        return self.name


