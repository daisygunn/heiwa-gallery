from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user_account.views import (account_overview, user_profile_display,
                                user_orders, add_to_wishlist, user_wishlist,
                                remove_from_wishlist)


# Create your tests here
class TestProductsUrls(SimpleTestCase):
    """ Products app url tests """
    def test_account_overview_url_is_resolved(self):
        """ account_overview list """
        url = reverse('account_overview')
        self.assertEqual(resolve(url).func, account_overview)

    def test_user_profile_display_url_is_resolved(self):
        """ user_profile_display url """
        url = reverse('user_profile')
        self.assertEqual(resolve(url).func, user_profile_display)

    def test_user_orders_url_is_resolved(self):
        """ user_orders url """
        url = reverse('user_orders')
        self.assertEqual(resolve(url).func, user_orders)

    def test_wishlist_url_is_resolved(self):
        """ wishlist """
        url = reverse('wishlist')
        self.assertEqual(resolve(url).func, user_wishlist)

    def test_add_to_wishlist_url_is_resolved(self):
        """ add_to_wishlist """
        url = reverse('add_to_wishlist', args=['pk'])
        self.assertEqual(resolve(url).func, add_to_wishlist)

    def test_remove_from_wishlist_url_is_resolved(self):
        """ remove_from_wishlist """
        url = reverse('remove_from_wishlist', args=['pk'])
        self.assertEqual(resolve(url).func, remove_from_wishlist)
