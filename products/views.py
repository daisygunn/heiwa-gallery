from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views import View
# from django.http import HttpResponseRedirect
from django.contrib import messages
# from django.contrib.auth.models import User
from .models import Product
from .forms import ProductForm, EditProductForm


class AllProducts(View):
    """ A view to return the all_products page """
    def get(self, request):
        """ get request """
        style = None
        products = Product.objects.all()

        if 'style' in request.GET:
            # get the style id from url
            style = request.GET['style']
            # filter using this id
            products = products.filter(style=style)
        # paginate by 12 products
        paginator = Paginator(products, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'products/all_products.html',
                      {'products': products,
                       'page_obj': page_obj})


class AddProduct(View):
    """ A view to return the all_products page """
    def get(self, request):
        """ get request """
        if not request.user.is_superuser:
            messages.error(request,
                           "You are not authorised to view that page.")
            return redirect(reverse('home'))
        else:
            add_product_form = ProductForm()
            return render(request, 'products/add_product.html',
                          {'add_product_form': add_product_form, })

    def post(self, request, *args, **kwargs):
        """ post view """
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.change_stock_label()
            product.save()
            messages.success(
                request, f"success, {product.name} has been added.")
            return redirect(reverse('all_products'))
        else:
            messages.success(request, "something went wrong...")
            return redirect(reverse('add_product'))


class UpdateProduct(View):
    """ A view to return the update_products page """
    def get(self, request):
        # IF NOT SUPERUSER
        if not request.user.is_superuser:
            messages.error(request,
                           "You are not authorised to view that page.")
            return redirect(reverse('home'))
        else:
            products = Product.objects.all()
            # paginate by 12 products
            paginator = Paginator(products, 12)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'products/update_products.html',
                          {'products': products,
                           'page_obj': page_obj})


class EditProduct(View):
    """ A view to return the edit_product page """
    def get(self, request, pk):
        """ get request """
        if not request.user.is_superuser:
            messages.error(request,
                           "You are not authorised to view that page.")
            return redirect(reverse('home'))
        else:
            product = get_object_or_404(Product, pk=pk)
            edit_product_form = EditProductForm(instance=product)
            return render(request, 'products/edit_product.html',
                          {'edit_product_form': edit_product_form, 'product': product })

    def post(self, request, pk, *args, **kwargs):
        """ post view """
        product = get_object_or_404(Product, pk=pk)
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"success, {product.name} has been updated.")
            return redirect(reverse('update_products'))
        else:
            form = EditProductForm(instance=product)
            messages.success(request, "something went wrong...")
            return redirect(reverse('edit_product'))

class StockManagement(View):
    """ A view to return the all_products page """
    def get(self, request):
        """ get request """
        if not request.user.is_superuser:
            messages.error(
                request, "You are not authorised to view that page.")
            return redirect(reverse('home'))
        else:
            return render(request, 'products/stock.html')
