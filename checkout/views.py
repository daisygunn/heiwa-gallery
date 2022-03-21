from django.shortcuts import render
from django.views import View
from .forms import OrderForm


class Checkout(View):
    """ checkout view """
    def get(self, request):
        """ get request """
        order_form = OrderForm()
        return render(request, 'checkout/checkout.html', {'form': order_form,})
