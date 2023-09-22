from django.contrib import admin
from .models import Cours, ImageCours
# Register your models here.


class ImageCoursInline(admin.TabularInline):
    model = ImageCours
 
    
@admin.register(Cours)
class AdminCours(admin.ModelAdmin):
    inlines = [
        ImageCoursInline,
    ]
    list_display = ['nom', 'description']
    



