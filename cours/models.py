from django.db import models
from django.urls import reverse

# Create your models here.
class Cours(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    
    
    def get_absolute_url(self):
        return reverse("cours-detail", kwargs={"pk": self.pk})


class ImageCours(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='media')   