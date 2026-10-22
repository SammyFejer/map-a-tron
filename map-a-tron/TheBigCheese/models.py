from django.db import models

# Create your models here.


class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='images/')
