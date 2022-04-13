from django.test import TestCase, Client
from django.urls import reverse


class TestHomeViews(TestCase):
    """ home app view tests """
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('home')
        self.about_url = reverse('about')

    def test_home_GET(self):
        """ get home view """
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_about_page_GET(self):
        """ get about page view """
        response = self.client.get(self.about_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')
