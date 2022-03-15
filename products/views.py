from django.shortcuts import render, reverse, redirect
from django.core.paginator import Paginator
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Product
from .forms import AddProductForm


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
            add_product_form = AddProductForm()
            return render(request, 'products/add_product.html',
                        {'add_product_form': add_product_form,
                        })
    def post(self, request, *args, **kwargs):
        """ post view """
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.change_stock_label()
            product.save()
            messages.success(request, f"success, {product.name} has been added.")
            return redirect(reverse('all_products'))
        else:
            messages.success(request, "something went wrong...")
            return redirect(reverse('add_product'))


class StockManagement(View):
    """ A view to return the all_products page """
    def get(self, request):
        """ get request """
        if not request.user.is_superuser:
            messages.error(request,
                            "You are not authorised to view that page.")
            return redirect(reverse('home'))
        else:
            return render(request, 'products/stock.html')
