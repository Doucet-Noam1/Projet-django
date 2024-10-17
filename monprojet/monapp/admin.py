from django.contrib import admin
from .models import Product, ProductItem, ProductAttribute, ProductAttributeValue, Fournisseurs, ProductFournisseur, Commande, CommandeItem


def set_product_online(modeladmin, request, queryset):
    queryset.update(status=1)


set_product_online.short_description = "Mettre en ligne"


def set_product_offline(modeladmin, request, queryset):
    queryset.update(status=0)


set_product_offline.short_description = "Mettre hors ligne"


class ProductItemAdmin(admin.TabularInline):
    model = ProductItem
    filter_vertical = ("attributes",)
    raw_id_fields = ["attributes"]


class ProductFilter(admin.SimpleListFilter):
    title = "filtre produit"
    parameter_name = "custom_status"

    def lookups(self, request, model_admin):
        return (
            ("online", "En ligne"),
            ("offline", "Hors ligne"),
        )

    def queryset(self, request, queryset):
        if self.value() == "online":
            return queryset.filter(status=1)
        if self.value() == "offline":
            return queryset.filter(status=0)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [
        ProductItemAdmin,
    ]
    list_filter = (ProductFilter,)
    actions = [set_product_online, set_product_offline]
    # Remplacer ou supprimer 'price_ht' et 'price_ttc'
    list_display = ["code", "name"]  # Enlève 'price_ht', 'price_ttc', et 'tax'
    list_editable = ["name"]  # Enlève 'price_ht' et 'price_ttc'

    # Si tu veux calculer les taxes, assure-toi que tu utilises des champs valides
    #def tax(self, instance):
    #    return ((instance.price_ttc / instance.price_ht) - 1) * 100
    #tax.short_description = "Taxes (%)"
    #tax.admin_order_field = "price_ht"

class ProductFournisseurInline(admin.TabularInline):
    model = ProductFournisseur
    extra = 1  # Permet d'ajouter facilement des prix pour les fournisseurs

class FournisseurAdmin(admin.ModelAdmin):
    model = Fournisseurs
    search_fields = ["name"]  # Ajout d'un champ de recherche par nom
    list_display = ["name"]  # Affiche le nom du fournisseur dans la liste
    inlines = [
        ProductFournisseurInline,  # Affiche les produits liés au fournisseur
    ]
class CommandeItemInline(admin.TabularInline):
    model = CommandeItem
    extra = 1  # Ajouter des articles à la commande

class CommandeAdmin(admin.ModelAdmin):
    model = Commande
    list_display = ["id", "fournisseur", "status", "date_commande"]  # Champs affichés dans la liste des commandes
    list_filter = ["status", "date_commande"]  # Filtres pour filtrer par statut et date
    search_fields = ["fournisseur__name"]  # Recherche par nom de fournisseur
    date_hierarchy = "date_commande"  # Navigation par dates dans la liste
    inlines = [
        CommandeItemInline,  # Permet de gérer les articles dans une commande
    ]
    actions = ["set_status_recue"]

    # Action personnalisée pour changer le statut à "Reçue"
    def set_status_recue(self, request, queryset):
        queryset.update(status=2)

    set_status_recue.short_description = "Marquer comme reçue"
admin.site.register(Commande, CommandeAdmin)
admin.site.register(Fournisseurs, FournisseurAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductItem)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
