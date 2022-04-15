from django.test import TestCase, Client
from .models import Exhibitions
# import datetime


class TestExhibitionsViews(TestCase):
    """ exhibitions app view tests """
    def setUp(self):
        self.client = Client()
        self.exhibition1 = Exhibitions.objects.create(
            name='Test 1234',
            style='sculpture',
            description='Lorem Ipsum',
            photographer_artist='Tester tester',
            entrance_fee=12.00,
            gallery_area='main gallery',
            display=True,
            date_starting='2022-05-20',
            date_finishing='2022-06-22',
        )

    def test_exhibition_name(self):
        exhibition = self.exhibition1
        self.assertEqual(str(exhibition), 'Test 1234 by Tester tester')

    # def test_exhibition_status_label(self):
    #     exhibition = self.exhibition1
    #     exhibition.date_starting = datetime.datetime.strptime(
    #             self.exhibition1.date_starting, "%d/%m/%Y").date()
    #     exhibition.date_finishing = datetime.datetime.strptime(
    #             self.exhibition1.date_finishing, "%d/%m/%Y").date()
    #     exhibition.now_showing_calc()
    #     self.assertEqual(exhibition.status, 'coming soon')
