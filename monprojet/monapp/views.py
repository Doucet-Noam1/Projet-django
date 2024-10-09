from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.generic import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import ContactUsForm, ProductForm
from django.forms import BaseModelForm
from django.urls import reverse_lazy
from .models import *

# Create your views here.


class ProductItemListView(ListView):
    model = ProductItem
    template_name = "monapp/list_items.html"
    context_object_name = "productitems"
    def get_queryset(self ):
        return ProductItem.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ProductItemListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des déclinaisons"
        return context


class ProductItemDetailView(DetailView):
    model = ProductItem
    template_name = "monapp/detail_item.html"
    context_object_name = "productitem"
    def get_context_data(self, **kwargs):
        context = super(ProductItemDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail déclinaison"
        # Récupérer les attributs associés à cette déclinaison
        context['attributes'] = self.object.attributes.all()
        return context

# class ProductAttributeListView(ListView):
#     model = ProductAttribute
#     template_name = "monapp/list_product_attributes.html"
#     context_object_name = "product_attributes"

#     def get_context_data(self, **kwargs):
#         context = super(ProductAttributeListView, self).get_context_data(**kwargs)
#         context["titremenu"] = "Liste des attributs de produit"
#         return context


# class ProductAttributeDetailView(DetailView):
#     model = ProductAttribute
#     template_name = "monapp/detail_product_attribute.html"
#     context_object_name = "product_attribute"

#     def get_context_data(self, **kwargs):
#         context = super(ProductAttributeDetailView, self).get_context_data(**kwargs)
#         context["titremenu"] = "Détail attribut produit"
#         return context

class ProductAttributeDetailView(DetailView):
    model = ProductAttribute
    template_name = "monapp/detail_attribute.html"
    context_object_name = "productattribute"
    def get_context_data(self, **kwargs):
        context = super(ProductAttributeDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail attribut"
        context['values']=ProductAttributeValue.objects.filter(product_attribute=self.object).order_by('position')
        return context


class ProductListView(ListView):
    model = Product
    template_name = "monapp/list_products.html"
    context_object_name = "products"
    def get_queryset(self):
        # Surcouche pour filtrer les résultats en fonction de la recherche
        # Récupérer le terme de recherche depuis la requête GET
        query = self.request.GET.get('search')
        if query:
            # Filtre les produits par nom (insensible à la casse)
            return Product.objects.filter(name__icontains=query)
        # Si aucun terme de recherche, retourner tous les produits
        return Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des produits"
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "monapp/detail_product.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["titremenu"] = "Détail produit"
        return context


class HomeView(TemplateView):
    template_name = "monapp/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["titreh1"] = "Hello"
        context["param"] = self.kwargs.get("param", "")
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)


class AboutView(TemplateView):
    template_name = "monapp/home.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context["titreh1"] = "About us..."
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)


def ContactView(request):
    titreh1 = "Contact us !"
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MonProjet Contact Us form',
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@monprojet.com"],
            )
    else:
        form = ContactUsForm()
    return render(request, "monapp/contact.html", {"titreh1": titreh1, "form": form})


class ConnectView(LoginView):
    template_name = "monapp/login.html"

    def post(self, request, **kwargs):
        username = request.POST.get("username", False)
        password = request.POST.get("password", False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return render(
                request,
                "monapp/hello.html",
                {"titreh1": "hello " + username + ", you're connected"},
            )
        else:
            return render(request, "monapp/register.html")


class RegisterView(TemplateView):
    template_name = "monapp/register.html"

    def post(self, request, **kwargs):
        username = request.POST.get("username", False)
        mail = request.POST.get("mail", False)
        password = request.POST.get("password", False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, "monapp/login.html")
        else:
            return render(request, "monapp/register.html")


class DisconnectView(TemplateView):
    template_name = "monapp/logout.html"

    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)

def ProductCreate(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product-detail', product.id)
    else:
        form = ProductForm()
    return render(request, "monapp/new_product.html", {'form': form})

class ProductCreateView(CreateView):
    model = Product
    form_class=ProductForm
    template_name = "monapp/new_product.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product = form.save()
        return redirect('product-detail', product.id)

class ProductUpdateView(UpdateView):
    model = Product
    form_class=ProductForm
    template_name = "monapp/update_product.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product = form.save()
        return redirect('product-detail', product.id)
    
class ProductDeleteView(DeleteView):
    model = Product
    template_name = "monapp/delete_product.html"
    success_url = reverse_lazy('product-list')

class ProductAttributeListView(ListView):
    model = ProductAttribute
    template_name = "monapp/list_attributes.html"
    context_object_name = "productattributes"
    def get_queryset(self ):
        return ProductAttribute.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ProductAttributeListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des attributs"
        return context