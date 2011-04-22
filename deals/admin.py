from django.contrib import admin
from deals.models import *

class MagasinAdmin(admin.ModelAdmin):
    list_display = ("nom", "tel", "fax", "region")
    
class ProduitAdmin(admin.ModelAdmin):
    list_display = ("nom", "date_debut", "date_fin", "region", "magasin", "categorie")

admin.site.register(Region)
admin.site.register(Categorie)
admin.site.register(Magasin, MagasinAdmin)
admin.site.register(Produit, ProduitAdmin)



