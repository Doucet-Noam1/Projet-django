from django import forms
from .models import Product, ProductAttributeValue,Commande,Fournisseurs

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        #fields = '__all__'
        exclude = ('price_ttc', 'status')


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