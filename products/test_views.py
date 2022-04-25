from django.test import TestCase, Client
from django.urls import reverse
from .models import Product, Category
from django.contrib.auth.models import User


class TestProductsViews(TestCase):
    """ products app view tests """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='project.test@test.com',
            email='project.test@test.com', password='12345')
        self.client.login(
            username='project.test@test.com',
            email='project.test@test.com', password='12345')

        self.category1 = Category.objects.create(
            category_name='b+w'
        )
        self.category2 = Category.objects.create(
            category_name='graphic art',
        )
        self.product1 = Product.objects.create(
            name='Test 1234',
            category=self.category1,
            photographer_artist='Tester tester',
            size='A4',
            quantity_in_stock=5,
            price=15.00,
        )

        self.product2 = Product.objects.create(
            name='Test 123456',
            category=self.category2,
            photographer_artist='Tester Smith',
            size='A4',
            quantity_in_stock=5,
            price=15.00,
        )

        self.all_products_url = reverse('all_products')
        self.add_product_url = reverse('add_product')
        self.product_management_url = reverse('product_management')
        self.edit_product_url = reverse(
            'edit_product', args=[self.product1.pk])
        self.delete_product_url = reverse(
            'delete_product', args=[self.product1.pk])
        self.edit_product2_url = reverse(
            'edit_product', args=[self.product2.pk])
        self.delete_product2_url = reverse(
            'delete_product', args=[self.product2.pk])
        # self.stock_url = reverse('stock', pk=self.product1.pk)

    def test_all_products_GET(self):
        """ get all products view """
        response = self.client.get(self.all_products_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products.html')

    def test_add_products_superuser_GET(self):
        """ get add_products view for superuser """
        response = self.client.get(self.add_product_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_add_product_not_superuser_GET(self):
        """ get add_product view """
        self.client.logout()
        response = self.client.get(self.add_product_url)

        self.assertEqual(response.status_code, 302)

    def test_product_management_superuser_GET(self):
        """ get product_management view for superuser """
        response = self.client.get(self.product_management_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_management.html')

    def test_product_management_not_superuser_GET(self):
        """ get product_management view """
        self.client.logout()
        response = self.client.get(self.product_management_url)

        self.assertEqual(response.status_code, 302)

    def test_edit_product_superuser_GET(self):
        """ get edit_product view for superuser """
        response = self.client.get(self.edit_product_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_edit_product_not_superuser_GET(self):
        """ get edit_product view for logged out user """
        self.client.logout()
        response = self.client.get(self.edit_product_url)

        self.assertEqual(response.status_code, 302)

    def test_delete_product_superuser_GET(self):
        """ get delete_products view for superuser """
        response = self.client.get(self.delete_product_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/delete_product.html')

    def test_delete_product_not_superuser_GET(self):
        """ get delete_product view for logged out user """
        self.client.logout()
        response = self.client.get(self.delete_product_url)

        self.assertEqual(response.status_code, 302)

    def test_add_product_superuser_POST(self):
        """ post add_product view for superuser """
        product3 = Product.objects.create(
            name='TestA6',
            category=self.category2,
            photographer_artist='Anne Smith',
            size='A6',
            quantity_in_stock=9,
            price=24.00,
        )
        product3.change_stock_label()
        product3.save()
        response = self.client.post(
            self.add_product_url, {product3: product3, })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(product3.in_stock, True)
        self.assertRedirects(response, reverse('add_product'))
        self.assertEqual(len(Product.objects.all()), 3)
