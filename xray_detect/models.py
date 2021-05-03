from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class xray(models.Model):
    image = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.image

    class Meta:
        ordering = ('image', )