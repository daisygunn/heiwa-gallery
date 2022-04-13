from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (AllProducts, AddProduct,
                            UpdateProduct, EditProduct,
                            DeleteProduct, StockManagement)


# Create your tests here
class TestProductsUrls(SimpleTestCase):
    """ Products app url tests """
    def test_all_products_url_is_resolved(self):
        """ all products list """
        url = reverse('all_products')
        self.assertEqual(resolve(url).func.view_class, AllProducts)

    def test_add_product_url_is_resolved(self):
        """ adding an product """
        url = reverse('add_product')
        self.assertEqual(resolve(url).func.view_class, AddProduct)

    def test_update_products_url_is_resolved(self):
        """ editing an product """
        url = reverse('update_products')
        self.assertEqual(resolve(url).func.view_class, UpdateProduct)

    def test_edit_product_url_is_resolved(self):
        """ editing a product """
        url = reverse('edit_product', args=['pk'])
        self.assertEqual(resolve(url).func.view_class, EditProduct)

    def test_delete_product_url_is_resolved(self):
        """ deleting a product """
        url = reverse('delete_product', args=['pk'])
        self.assertEqual(resolve(url).func.view_class, DeleteProduct)

    def test_stock_url_is_resolved(self):
        """ changing stock level of a product """
        url = reverse('stock', args=['pk'])
        self.assertEqual(resolve(url).func.view_class, StockManagement)
