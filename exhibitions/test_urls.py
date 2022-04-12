from django.test import SimpleTestCase
from django.urls import reverse, resolve
from exhibitions.views import (exhibitions_list, AddExhibition,
                               EditExhibition, DeleteExhibition)


# Create your tests here
class TestExhibitionsUrls(SimpleTestCase):
    def test_exhibitions_list_url_is_resolved(self):
        url = reverse('exhibitions_list')
        self.assertEquals(resolve(url).func, exhibitions_list)

    def test_add_exhibition_url_is_resolved(self):
        url = reverse('add_exhibition')
        self.assertEquals(resolve(url).func.view_class, AddExhibition)

    def test_edit_exhibition_url_is_resolved(self):
        url = reverse('edit_exhibition', args=['pk'])
        self.assertEquals(resolve(url).func.view_class, EditExhibition)

    def test_delete_exhibition_url_is_resolved(self):
        url = reverse('delete_exhibition', args=['pk'])
        self.assertEquals(resolve(url).func.view_class, DeleteExhibition)