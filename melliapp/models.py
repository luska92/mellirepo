from django.db import models
import os
from django.urls import reverse


class Produkt(models.Model):
    name = models.CharField(max_length=256)
    price = models.PositiveIntegerField()
    desc = models.CharField(max_length=256)
    size1 = models.CharField(max_length=256)
    size2 = models.CharField(max_length=256)
    size3 = models.CharField(max_length=256)
    color1 = models.CharField(max_length=256, blank=True, null=True)
    color2 = models.CharField(max_length=256, blank=True, null=True)
    color3 = models.CharField(max_length=256, blank=True, null=True)
    photo1 = models.ImageField(upload_to='melliapp/static/images', blank=True, null=True)
    photo2 = models.ImageField(upload_to='melliapp/static/images', blank=True, null=True)
    photo3 = models.ImageField(upload_to='melliapp/static/images', blank=True, null=True)
    photo4 = models.ImageField(upload_to='melliapp/static/images', blank=True, null=True)
    photo5 = models.ImageField(upload_to='melliapp/static/images', blank=True, null=True)

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse("basic_app:detail",kwargs={'pk':self.pk})
