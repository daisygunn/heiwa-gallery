from django.db import models

from datetime import datetime


exhibitions_type = (('photography', 'photography'),
                    ('sculpture', 'sculpture'),
                    ('painting', 'painting'),
                    ('video', 'video'),
                    )

areas = (('main gallery', 'main gallery'),
         ('studio', 'studio'),
         ('basement', 'basement'),)

status = (('finished', 'finished'),
          ('now showing', 'now showing'),
          ('coming soon', 'coming soon'),
          ('pending', 'pending'),
          ('cancelled', 'cancelled'))


class Exhibitions(models.Model):
    """ exhibitions model """
    class Meta:
        """ override plural name """
        verbose_name_plural = 'Exhibitions'

    name = models.CharField(max_length=254, null=False, blank=False)
    style = models.CharField(max_length=254, choices=exhibitions_type, default=1)
    description = models.TextField(null=True, blank=True)
    photographer_artist = models.CharField(max_length=254, blank=True)
    entrance_fee = models.DecimalField(max_digits=6, decimal_places=2)
    gallery_area = models.CharField(
        max_length=254, choices=areas, default='main gallery')
    display = models.BooleanField(default=False)
    status = models.CharField(
        max_length=254, choices=status, default='now showing')
    date_starting = models.DateField(null=True, blank=True)
    date_finishing = models.DateField(null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.photographer_artist}"

    def now_showing_calc(self):
        """ set now showing """
        start_date = self.date_starting
        end_date = self.date_finishing

        # create datetime objects from the strings
        start = start_date
        end = end_date
        now = datetime.now().date()

        if start == "":
            self.status = 'pending'
        elif end == "":
            self.status = 'pending'
        elif end < now:
            self.status = 'finished'
        elif start > now:
            self.status = 'coming soon'
        else:
            self.status = 'now showing'

    def start_end_validation(self):
        """ set now showing """
        start_date = self.date_starting
        end_date = self.date_finishing

        if start_date > end_date:
            return False
        else:
            return True
