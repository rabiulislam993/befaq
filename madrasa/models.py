from django.db import models


class Madrasa(models.Model):
    name      = models.CharField(max_length=127)
    address   = models.CharField(max_length=255, blank=True)
    is_markaz = models.BooleanField(default=False)

    def __str__(self):
        return self.name