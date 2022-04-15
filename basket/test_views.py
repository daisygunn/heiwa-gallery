from django.test import TestCase, Client
from django.urls import reverse


class TestBasketView(TestCase):
    """ test basket view """
    def test_get_basket_overview(self):
        self.client = Client()
        response = self.client.get(reverse('basket_overview'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')
