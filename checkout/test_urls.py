from django.test import SimpleTestCase
from django.urls import reverse, resolve
from checkout.views import (checkout_success, cache_checkout_data,
                          checkout)
from .webhooks import webhook


class TestCheckoutUrls(SimpleTestCase):
    """ url tests for checkout app """
    def test_checkout_url_is_resolved(self):
        """ checkout page """
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)

    def test_checkout_success_url_is_resolved(self):
        """ successful checkout """
        url = reverse('checkout_success', args=['order_number'])
        self.assertEqual(resolve(url).func, checkout_success)

    def test_cache_checkout_data_url_is_resolved(self):
        """ caching checkout data  """
        url = reverse('cache_checkout_data')
        self.assertEqual(resolve(url).func, cache_checkout_data)

    def test_webhook_url_is_resolved(self):
        """ webhook """
        url = reverse('webhook')
        self.assertEqual(resolve(url).func, webhook)