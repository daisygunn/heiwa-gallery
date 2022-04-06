from django.db import models

from datetime import datetime


exhibitions_type = (('photography', 'photography'),
                    ('sculpture', 'sculpture'),
                    ('painting', 'painting'),
                    ('video', 'video'),
                    )

areas = (('1', '1'),
         ('2', '2'),
         ('3', '3'),)


class Exhibitions(models.Model):
    """ exhibitions model """
    class Meta:
        """ override plural name """
        verbose_name_plural = 'Exhibitions'

    name = models.CharField(max_length=254)
    style = models.CharField(max_length=254, choices=exhibitions_type, default=1)
    description = models.TextField()
    photographer_artist = models.CharField(max_length=254, blank=True)
    entrance_fee = models.DecimalField(max_digits=6, decimal_places=2)
    gallery_area = models.CharField(max_length=254, choices=areas, default=1)
    now_showing = models.BooleanField(default=False)
    date_starting = models.DateField()
    date_finishing = models.DateField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.photographer_artist}"

    def now_showing_calc(self):
        """ set now showing """
        start_date = self.date_starting
        end_date = self.date_finishing

        # format of date/time strings; assuming dd/mm/yyyy
        date_format = "%d/%m/%Y %H:%M:%S"

        # create datetime objects from the strings
        start = datetime.strptime(start_date, date_format)
        end = datetime.strptime(end_date, date_format)
        now = datetime.now()

        if end < now:
            self.now_showing = False
        elif start > now:
            self.now_showing = False
        else:
            self.now_showing = True
