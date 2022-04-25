from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import UserProfile, UserWishlist
from products.models import Product, Category


class TestUserAccountViews(TestCase):
    """ user account app view tests """
    def setUp(self):
        self.client = Client()
        self.category1 = Category.objects.create(
            category_name='b+w',
            name_to_display='Black and White'
        )
        self.product1 = Product.objects.create(
            name='Test 1234',
            category=self.category1,
            photographer_artist='Tester tester',
            size='A4',
            quantity_in_stock=5,
            price=15.00,
        )
        self.user = User(username='project.test@test.com')
        self.user_profile = UserProfile(
            user=self.user, email='project.test@test.com')

    def test_user_profile_name(self):
        user_profile = self.user_profile
        self.assertEqual(
            str(user_profile), 'project.test@test.com')

    def test_user_wishlist(self):
        user_wishlist = UserWishlist(
            user=self.user_profile, product=self.product1)
        self.assertEqual(str(user_wishlist), 'Test 1234')
