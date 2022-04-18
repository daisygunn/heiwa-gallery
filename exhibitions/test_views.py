from django.test import TestCase, Client
from django.urls import reverse
from .models import Exhibitions
from django.contrib.auth.models import User


class TestExhibitionsViews(TestCase):
    """ exhibitions app view tests """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='project.test@test.com',
            email='project.test@test.com', password='12345')
        self.client.login(
            username='project.test@test.com',
            email='project.test@test.com', password='12345')
        self.exhibition1 = Exhibitions.objects.create(
            name='Test 1234',
            style='sculpture',
            description='Lorem Ipsum',
            photographer_artist='Tester tester',
            entrance_fee=12.00,
            gallery_area='main gallery',
            display=True,
            date_starting='2022-05-20',
            date_finishing='2022-06-20',
        )

        self.exhibition2 = Exhibitions.objects.create(
            name='Testingtestign',
            style='sculpture',
            description='Lorem Ipsum',
            photographer_artist='Tester',
            entrance_fee=18.00,
            gallery_area='main gallery',
            display=True,
            date_starting='2022-08-20',
            date_finishing='2022-10-20',
        )

        self.exhibitions_list_url = reverse('exhibitions_list')
        self.exhibition_management_url = reverse('exhibition_management')
        self.add_exhibition_url = reverse('add_exhibition')
        self.edit_exhibition_url = reverse('edit_exhibition', args=[1])
        self.delete_exhibition_url = reverse('delete_exhibition', args=[1])
        self.edit_exhibition2_url = reverse('edit_exhibition', args=[2])
        self.delete_exhibition2_url = reverse('delete_exhibition', args=[2])

    def test_exhibitions_list_GET(self):
        """ get exhibitions list view """
        response = self.client.get(self.exhibitions_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exhibitions/exhibitions.html')

    def test_add_exhibition_superuser_GET(self):
        """ get add_exhibitionl view for superuser """
        response = self.client.get(self.add_exhibition_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exhibitions/add_exhibition.html')

    def test_add_exhibition_not_superuser_GET(self):
        """ get add_exhibition view """
        self.client.logout()
        response = self.client.get(self.add_exhibition_url)

        self.assertEqual(response.status_code, 302)

    def test_edit_exhibition_superuser_GET(self):
        """ get edit_exhibition view for superuser """
        response = self.client.get(self.edit_exhibition_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exhibitions/edit_exhibition.html')

    def test_edit_exhibition_not_superuser_GET(self):
        """ get edit_exhibition view for logged out user """
        self.client.logout()
        response = self.client.get(self.edit_exhibition_url)

        self.assertEqual(response.status_code, 302)

    def test_delete_exhibition_superuser_GET(self):
        """ get delete_exhibition view for superuser """
        response = self.client.get(self.delete_exhibition_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exhibitions/delete_exhibition.html')

    def test_delete_exhibition_not_superuser_GET(self):
        """ get delete_exhibition view for logged out user """
        self.client.logout()
        response = self.client.get(self.delete_exhibition_url)

        self.assertEqual(response.status_code, 302)

    def test_exhibition_management_superuser_GET(self):
        """ get exhibition_management view for superuser """
        response = self.client.get(self.exhibition_management_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'exhibitions/exhibition_management.html')

    def test_exhibition_management_not_superuser_GET(self):
        """ get exhibition_management view for logged out user """
        self.client.logout()
        response = self.client.get(self.exhibition_management_url)

        self.assertEqual(response.status_code, 302)

    def test_add_exhibition_not_superuser_POST(self):
        """ get add_exhibition view """
        self.client.logout()
        response = self.client.post(self.add_exhibition_url)

        self.assertEqual(response.status_code, 302)

    def test_add_exhibition_superuser_POST(self):
        """ post add_exhibition view for superuser """
        exhibition3 = Exhibitions.objects.create(
            name='Test2 1234',
            style='photography',
            description='Lorem Ipsum',
            photographer_artist='Tester tester',
            entrance_fee=15.00,
            gallery_area='studio',
            display=True,
            date_starting='2022-04-01',
            date_finishing='2022-08-15',
        )
        exhibition3.save()
        response = self.client.post(self.add_exhibition_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('add_exhibition'))
        self.assertEqual(len(Exhibitions.objects.all()), 3)

    def test_edit_exhibition_not_superuser_POST(self):
        """ get edit_exhibition view """
        self.client.logout()
        response = self.client.post(self.edit_exhibition_url)

        self.assertEqual(response.status_code, 302)

    def test_edit_exhibition_superuser_POST(self):
        """ post edit_exhibition view for superuser """
        exhibition = self.exhibition1
        exhibition.name = 'Name has changed'

        response = self.client.post(self.edit_exhibition_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.exhibition1.name, 'Name has changed')

    def test_delete_exhibition_not_superuser_POST(self):
        """ get delete_exhibition view """
        self.client.logout()
        response = self.client.post(self.delete_exhibition_url)

        self.assertEqual(response.status_code, 302)

    def test_delete_exhibition_superuser_POST(self):
        """ post delete_exhibition view for superuser """
        exhibition = self.exhibition2

        response = self.client.post(self.delete_exhibition2_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Exhibitions.objects.all()), 1)
        self.assertNotIn(self.exhibition2, Exhibitions.objects.all())
