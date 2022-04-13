from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index, about


# Create your tests here
class TestHomeUrls(SimpleTestCase):
    """ home app url tests """
    def test_home_url_is_resolved(self):
        """ index page """
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

    def test_about_url_is_resolved(self):
        """ about page """
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)
