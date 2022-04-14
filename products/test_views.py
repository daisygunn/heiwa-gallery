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
            style=self.category1,
            photographer_artist='Tester tester',
            size='A4',
            quantity_in_stock=5,
            price=15.00,
        )

        self.product2 = Product.objects.create(
            name='Test 1234',
            style=self.category2,
            photographer_artist='Tester Smith',
            size='A4',
            quantity_in_stock=5,
            price=15.00,
        )

        self.all_products_url = reverse('all_products')
        self.add_product_url = reverse('add_product')
        self.update_products_url = reverse('update_products')
        self.edit_product_url = reverse(
            'edit_product', args=[self.product1.pk])
        self.delete_product_url = reverse(
            'delete_product', args=[self.product1.pk])
        self.edit_product2_url = reverse(
            'edit_product', args=[self.product2.pk])
        self.delete_product2_url = reverse(
            'delete_product', args=[self.product2.pk])

    def test_all_products_GET(self):
        """ get all products view """
        response = self.client.get(self.all_products_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products.html')

    def test_add_products_superuser_GET(self):
        """ get add_productsl view for superuser """
        response = self.client.get(self.add_product_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')
    
    def test_add_product_not_superuser_GET(self):
        """ get add_product view """
        self.client.logout()
        response = self.client.get(self.add_product_url)

        self.assertEqual(response.status_code, 302)

    def test_update_products_superuser_GET(self):
        """ get update_products view for superuser """
        response = self.client.get(self.update_products_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/update_products.html')

    def test_update_products_not_superuser_GET(self):
        """ get update_products view """
        self.client.logout()
        response = self.client.get(self.update_products_url)

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
