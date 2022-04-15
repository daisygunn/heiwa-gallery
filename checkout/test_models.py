from django.test import TestCase, Client
from .models import Order, OrderItem
from products.models import Product, Category
from django.contrib.auth.models import User
from user_account.models import UserProfile


class TestCheckoutModels(TestCase):
    """ checkout app model test """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='project.test@test.com',
            email='project.test@test.com', password='12345')
        self.client.login(
            username='project.test@test.com',
            email='project.test@test.com', password='12345')
        self.user_profile = UserProfile.objects.get(user=self.user)
        self.order1 = Order.objects.create(
            user_profile=self.user_profile,
            full_name='Testington Test',
            email='test@test.com',
            phone_number='07969483821',
            flat_house='12',
            town_city='London',
            street_address='Test road',
            county='London',
            postcode='Nw3 4tn',
            country='United Kingdom',
            order_total=0,)
        self.category1 = Category.objects.create(
            category_name='b+w',
            name_to_display='Black and White'
        )
        self.product1 = Product.objects.create(
            name='Test 1234',
            style=self.category1,
            photographer_artist='Tester tester',
            size='A4',
            quantity_in_stock=5,
            price=15.00,
        )

        self.order_item1 = OrderItem.objects.create(
            order=self.order1,
            product=self.product1,
            quantity=3,)

    def test_order_name_is_order_number(self):
        order = self.order1
        order._generate_order_number()
        self.assertEqual(len(str(order)), 32)

    def test_full_address(self):
        order = self.order1
        full_address = order.full_address()
        self.assertEqual(
            full_address, "12, Test road, London, London, Nw3 4tn")

    def test_order_item_name(self):
        order_item = self.order_item1
        self.assertEqual(str(order_item), 'Test 1234 in A4')

    def test_order_item_save_updates_orderitem_total(self):
        order_item = self.order_item1
        order_item.save()
       
        self.assertEqual(self.order_item1.orderitem_total, 45.00)

    def test_order_item_save_updates_order_total(self):
        order = self.order1
        order.update_total()
        self.assertEqual(self.order1.order_total, 45.00)
