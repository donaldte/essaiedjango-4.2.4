from django.contrib import admin

from .models import Tache


@admin.register(Tache)
class AdminTache(admin.ModelAdmin):
    list_display = ['nom', 'description', 'date_creation', 'fait']