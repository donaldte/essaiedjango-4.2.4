from django.contrib import admin
from .models import Produit


admin.site.site_header = 'Formation django'
admin.site.site_title = 'Formation django'
admin.site.index_title = 'Formation django'

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prix', 'active', 'live']
    search_fields = ['nom', 'description']
    list_editable = ['nom', 'active']
    list_filter = ['prix', 'active', 'live', 'is_deleted']
    list_display_links = ['prix']
   
  
       
        

