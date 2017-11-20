from django.db import models
from django.shortcuts import reverse

class Madrasa(models.Model):
    name      = models.CharField(max_length=127, unique=True)
    address   = models.CharField(max_length=255, blank=True)
    is_markaz = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('madrasa:madrasa_detail', kwargs={'pk':self.pk})