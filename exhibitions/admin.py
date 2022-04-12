from django.contrib import admin
from .models import Exhibitions


@admin.register(Exhibitions)
class ExhibitionsAdmin(admin.ModelAdmin):
    """ Category admin management """
    list_display = ("name", "style", "photographer_artist",
                    "entrance_fee", "date_starting", "date_finishing", "status")
    