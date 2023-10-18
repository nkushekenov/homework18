from django.db import models
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

def get_absolute_url(self):
    return reverse('item_detail', args=[str(self.id)])
