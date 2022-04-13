from django.test import SimpleTestCase
from django.urls import reverse, resolve
from basket.views import (BasketOverview, add_product_to_basket,
                          remove_product, change_quantity)


# Create your tests here
class TestBasketUrls(SimpleTestCase):
    """ url tests for basket app """
    def test_basket_overview_url_is_resolved(self):
        """ basket overview """
        url = reverse('basket_overview')
        self.assertEquals(resolve(url).func.view_class, BasketOverview)

    def test_add_product_to_basket_url_is_resolved(self):
        """ add to basket basket """
        url = reverse('add_product_to_basket', args=['pk'])
        self.assertEquals(resolve(url).func, add_product_to_basket)

    def test_change_quantity_url_is_resolved(self):
        """ change quantity of product in basket """
        url = reverse('change_quantity', args=['pk'])
        self.assertEquals(resolve(url).func, change_quantity)

    def test_remove_product_url_is_resolved(self):
        """ remove product from basket """
        url = reverse('remove_product', args=['pk'])
        self.assertEquals(resolve(url).func, remove_product)