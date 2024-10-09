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
    ProductUpdateView
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("product-items/", ProductItemListView.as_view(), name="product-item-list"),
    path(
        "product-items/<int:pk>/",
        ProductItemDetailView.as_view(),
        name="product-item-detail",
    ),
    path(
        "product-attributes/",
        ProductAttributeListView.as_view(),
        name="product-attribute-list",
    ),
    path(
        "product-attributes/<int:pk>/",
        ProductAttributeDetailView.as_view(),
        name="product-attribute-detail",
    ),
    path("login/", ConnectView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", DisconnectView.as_view(), name="logout"),
    path("contact/", ContactView, name="contact"),
    path("product/<pk>/update/",ProductUpdateView.as_view(), name="product-update"),
    path("product/add/",ProductCreateView.as_view(), name="product-add"),
]
