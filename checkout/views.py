from django.shortcuts import render
from django.views import View
from .forms import OrderForm


class Checkout(View):
    """ checkout view """
    def get(self, request):
        """ get request """
        stripe_public_key = 'pk_test_51KUnvPHZrw79J0fC7O6xa3fvr9bSEYSORSfzvtSuM4b3LTvvRecG0SQslEbvfcQEamcTdyb46onuYHnPEw6xywum00frqppeEA'
        order_form = OrderForm()
        return render(request, 'checkout/checkout.html',
                      {'form': order_form,
                       'stripe_public_key': stripe_public_key})
