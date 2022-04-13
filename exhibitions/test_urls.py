from django.test import SimpleTestCase
from django.urls import reverse, resolve
from exhibitions.views import (exhibitions_list, AddExhibition,
                               EditExhibition, DeleteExhibition)


# Create your tests here
class TestExhibitionsUrls(SimpleTestCase):
    """ Exhibitions app url tests """
    def test_exhibitions_list_url_is_resolved(self):
        """ exhibitions list """
        url = reverse('exhibitions_list')
        self.assertEqual(resolve(url).func, exhibitions_list)

    def test_add_exhibition_url_is_resolved(self):
        """ adding an exhibition """
        url = reverse('add_exhibition')
        self.assertEqual(resolve(url).func.view_class, AddExhibition)

    def test_edit_exhibition_url_is_resolved(self):
        """ editing an exhibition """
        url = reverse('edit_exhibition', args=['pk'])
        self.assertEqual(resolve(url).func.view_class, EditExhibition)

    def test_delete_exhibition_url_is_resolved(self):
        """ deleting an exhibition """
        url = reverse('delete_exhibition', args=['pk'])
        self.assertEqual(resolve(url).func.view_class, DeleteExhibition)