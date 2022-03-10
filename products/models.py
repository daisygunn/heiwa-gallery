from django.db import models
from django.core.files.storage import FileSystemStorage


class Category(models.Model):
    """ category model """
    class Meta:
        """ override plural name """
        verbose_name_plural = 'Categories'

    category_name = models.CharField(max_length=50)
    name_to_display = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ programmatic name """
        return self.category_name

    def get_name_to_display(self):
        """ return name to display on site """
        return self.name_to_display


product_size_choices = (
    ("A5", "A5"),
    ("A4", "A4"),
    ("A3", "A3"),
    ("A2", "A2"),
)


class MediaFileSystemStorage(FileSystemStorage):
    """ stop files being renamed if they already exist """
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            return name

    def _save(self, name, content):
        if self.exists(name):
            # if the file exists, do not call the superclasses _save method
            return name
        # if the file is new, DO call it
        return super(MediaFileSystemStorage, self)._save(name, content)


class Product(models.Model):
    """ Product model """
    name = models.CharField(max_length=254)
    style = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True)
    photographer_artist = models.CharField(max_length=254, blank=True)
    size = models.CharField(
        max_length=2, choices=product_size_choices, default="A4")
    quantity_in_stock = models.IntegerField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(
        null=True, blank=True, storage=MediaFileSystemStorage())
    in_stock = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        """ return name to display on site """
        return self.name

    def get_product_id(self):
        """ return id to be referenced by """
        return self.pk

    def get_stock_level(self):
            """ get number in stock """
            return self.quantity_in_stock

    def change_to_out_of_stock(self):
            """ automatically change stock label """
            if self.quantity_in_stock < 1:
                self.in_stock = False
                self.save()

    def save(self, *args, **kwargs):
        if self.quantity_in_stock < 1:
                self.in_stock = False
        super(Product, self).save(*args, **kwargs)