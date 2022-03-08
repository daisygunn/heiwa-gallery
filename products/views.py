from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from .models import Product


class AllProducts(View):
    """ A view to return the all_products page """
    def get(self, request):
        """ get request """
        products = Product.objects.all()
        paginator = Paginator(products, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'products/all_products.html',
                      {'products': products, 
                      'page_obj': page_obj})
