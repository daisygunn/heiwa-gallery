from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
# from products.models import Product
from django.views import View


class BasketOverview(View):
    """ Returns basket page where overview 
    of customer basket is displayed """
    def get(self, request):
        """ get request """
        return render(request, 'basket/basket.html')
