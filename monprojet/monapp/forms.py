from django import forms
from .models import Product, ProductAttributeValue, Commande, Fournisseurs,CommandeItem,ProductFournisseur
from django.forms import modelformset_factory

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('price_ttc', 'status')

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code']  
    stock = forms.DecimalField(max_digits=8, decimal_places=2, required=True, label="Stock")
    fournisseur = forms.ModelChoiceField(queryset=Fournisseurs.objects.all(), required=True)
    price_ht = forms.DecimalField(max_digits=8, decimal_places=2, required=True, label="Prix unitaire HT")
    price_ttc = forms.DecimalField(max_digits=8, decimal_places=2, required=True, label="Prix unitaire TTC")

class ProductAttributeValueForm(forms.ModelForm):
    class Meta:
        model = ProductAttributeValue
        fields = "__all__"

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'

class FournisseursForm(forms.ModelForm):
    class Meta:
        model = Fournisseurs
        fields = '__all__'

class CommandeItemForm(forms.ModelForm):
    class Meta:
        model = CommandeItem
        fields = ['product', 'quantity']

    product = forms.ModelChoiceField(queryset=Product.objects.all(), required=True)
    quantity = forms.IntegerField(min_value=1, required=True)

 
class CommandeCreateForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['fournisseur'] 

    fournisseur = forms.ModelChoiceField(queryset=Fournisseurs.objects.all(), required=True)

class ProductFournisseurForm(forms.ModelForm):
    class Meta:
        model = ProductFournisseur
        fields = ['product', 'price_ht', 'price_ttc', 'stock']

CommandeItemFormSet = modelformset_factory(CommandeItem, form=CommandeItemForm, extra=1) 