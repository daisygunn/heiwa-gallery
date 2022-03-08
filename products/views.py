from django.shortcuts import render
from django.views import View
from .models import Product


class AllProducts(View):
    """ A view to return the index page """
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'products/all_products.html',
                      {'products': products})
