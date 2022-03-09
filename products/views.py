from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from .models import Product, Category


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
