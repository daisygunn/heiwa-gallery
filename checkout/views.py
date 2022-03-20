from django.shortcuts import render
from django.views import View


class Checkout(View):
    """ checkout view """
    def get(self, request):
        """ get request """
        return render(request, 'checkout/checkout.html')
