from django.test import TestCase
from .models import Product, Category


class TestProductsModels(TestCase):
    """ tests for the product model """
    def setUp(self):
        self.category1 = Category.objects.create(
            category_name='b+w',
            name_to_display='Black and White'
        )
        self.category2 = Category.objects.create(
            category_name='graphic_art',
            name_to_display='Graphic Art'
        )
        self.product1 = Product.objects.create(
            name='Test 1234',
            style=self.category1,
            photographer_artist='Tester tester',
            size='A4',
            quantity_in_stock=5,
            price=15.00,
        )

    def test_product_name(self):
        product = self.product1
        self.assertEqual(str(product), 'Test 1234')

    def test_stock_label_change(self):
        product = self.product1
        product.quantity_in_stock = 0
        product.change_stock_label()
        self.assertEqual(product.in_stock, False)

    def test_category_name(self):
        category = self.category1
        self.assertEqual(str(category), 'b+w')

    def test_category_name_to_display(self):
        category = self.category1
        display_name = category.get_name_to_display()
        self.assertEqual(display_name, 'Black and White')
