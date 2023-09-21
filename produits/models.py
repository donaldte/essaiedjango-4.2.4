from django.db import models
from django.urls import reverse

# Create your models here.

class Produit(models.Model):
    nom         = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True, default="pas de description")
    prix        = models.DecimalField(max_digits=10000, decimal_places=2)
    active      = models.BooleanField(default=True)
    live        = models.BooleanField(default=True)
    is_deleted  = models.BooleanField(null=True)
    
    def __str__(self):
        return self.nom
    
    def get_absolute_url_for_detail(self):
        return reverse("pages:product_detail", kwargs={"my_id": self.pk})
    
    # reverse("nom_de_la_vue", kwargs={"variable": self.pk})
    
    def get_absolute_url_for_delete(self):
        return reverse("pages:product_delete", kwargs={"my_id": self.pk})
    