from django.db import models
from django.utils import timezone

# Définition des états de commande
COMMANDE_STATUS = ((0, 'En préparation'), (1, 'Passée'), (2, 'Reçue'))

# Modèle pour les statuts
class Status(models.Model):
    numero = models.IntegerField()
    libelle = models.CharField(max_length=100)

    def get_libelle(self):
        return self.libelle

    def __str__(self):
        return "{0} {1}".format(self.numero, self.libelle)


# Modèle pour les produits
class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, null=True, blank=True, unique=True)

    def __str__(self):
        return "{0} {1}".format(self.name, self.code)


# Modèle pour les fournisseurs
class Fournisseurs(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Modèle pour gérer la relation entre les produits et les fournisseurs (prix, stock, etc.)
class ProductFournisseur(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseurs, on_delete=models.CASCADE)
    price_ht = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Prix unitaire HT"
    )
    price_ttc = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Prix unitaire TTC"
    )
    stock = models.IntegerField()
    date_creation = models.DateTimeField(default=timezone.now, verbose_name="Date création")

    class Meta:
        unique_together = ('product', 'fournisseur')

    def __str__(self):
        return f'{self.product.name} - {self.fournisseur.name}'


# Modèle pour les déclinaisons de produit (ex : couleur)
class ProductItem(models.Model):
    color = models.CharField(max_length=100)
    code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attributes = models.ManyToManyField("ProductAttributeValue", related_name="product_item", blank=True)

    def __str__(self):
        return "{0} {1}".format(self.color, self.code)


# Modèle pour les attributs de produit (ex : taille)
class ProductAttribute(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Modèle pour les valeurs des attributs de produit (ex : petite, moyenne, grande)
class ProductAttributeValue(models.Model):
    value = models.CharField(max_length=100)
    product_attribute = models.ForeignKey(ProductAttribute, verbose_name="Unité", on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField("Position", null=True, blank=True)

    def __str__(self):
        return "{0} [{1}]".format(self.value, self.product_attribute)


# Modèle pour les commandes
class Commande(models.Model):
    fournisseur = models.ForeignKey(Fournisseurs, on_delete=models.CASCADE)
    status = models.IntegerField(choices=COMMANDE_STATUS, default=0)
    date_commande = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Commande {self.id} - {self.fournisseur.name} - {self.get_status_display()}'

    def update_stock(self):
        if self.status == 2:  # Si la commande est reçue
            for item in self.commandeitems.all():
                product_fournisseur = ProductFournisseur.objects.get(product=item.product, fournisseur=self.fournisseur)
                product_fournisseur.stock += item.quantity
                product_fournisseur.save()


# Modèle pour les éléments de commande
class CommandeItem(models.Model):
    commande = models.ForeignKey(Commande, related_name="commandeitems", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity}x {self.product.name}'
