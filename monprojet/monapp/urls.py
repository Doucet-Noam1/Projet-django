from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    HomeView,
    ProductItemListView,
    ProductItemDetailView,
    ProductAttributeListView,
    ProductAttributeDetailView,
    ConnectView,
    RegisterView,
    DisconnectView,
    ContactView,
    ProductCreateView,
    ProductUpdateView,
    ProductAttributeValueCreateView,
    CommandeListView,         # Importer les nouvelles vues
    CommandeDetailView,
    CommandeCreateView,
    CommandeUpdateView,
    CommandeDeleteView,
    FournisseurListView,      # Importer les nouvelles vues
    FournisseurDetailView,
    FournisseurCreateView,
    FournisseurUpdateView,
    FournisseurDeleteView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("product-items/", ProductItemListView.as_view(), name="product-item-list"),
    path("product-items/<int:pk>/", ProductItemDetailView.as_view(), name="product-item-detail"),
    path("product-attributes/", ProductAttributeListView.as_view(), name="product-attribute-list"),
    path("product-attributes/<int:pk>/", ProductAttributeDetailView.as_view(), name="product-attribute-detail"),
    path("login/", ConnectView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", DisconnectView.as_view(), name="logout"),
    path("contact/", ContactView, name="contact"),
    path("product/<pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("product/add/", ProductCreateView.as_view(), name="product-add"),
    path("product-attributes/add/", ProductAttributeValueCreateView.as_view(), name="product-attribute-add"),

    # Ajout des routes pour Commande
    path("commandes/", CommandeListView.as_view(), name="commande-list"),
    path("commandes/<int:pk>/", CommandeDetailView.as_view(), name="commande-detail"),
    path("commandes/new/", CommandeCreateView.as_view(), name="commande-create"),
    path("commandes/<int:pk>/edit/", CommandeUpdateView.as_view(), name="commande-update"),
    path("commandes/<int:pk>/delete/", CommandeDeleteView.as_view(), name="commande-delete"),

    # Ajout des routes pour Fournisseur
    path("fournisseurs/", FournisseurListView.as_view(), name="fournisseur-list"),
    path("fournisseurs/<int:pk>/", FournisseurDetailView.as_view(), name="fournisseur-detail"),
    path("fournisseurs/new/", FournisseurCreateView.as_view(), name="fournisseur-create"),
    path("fournisseurs/<int:pk>/edit/", FournisseurUpdateView.as_view(), name="fournisseur-update"),
    path("fournisseurs/<int:pk>/delete/", FournisseurDeleteView.as_view(), name="fournisseur-delete"),
]
