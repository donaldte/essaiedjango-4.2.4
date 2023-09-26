from django.db import models
from django.urls import reverse



class Tache(models.Model):
    """
    Name: Tache
    Description: Model definition for Tache.
    Author: donald 
    """
    
    nom = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date_creation = models.DateField()
    fait = models.BooleanField(default=False)
    
    
    def get_absolute_url(self):
        return reverse("tache:tache_detail", kwargs={"pk": self.pk})
    
    def get_absolute_url_update(self):
        return reverse("tache:tache_modify", kwargs={'pk': self.pk})
    
    