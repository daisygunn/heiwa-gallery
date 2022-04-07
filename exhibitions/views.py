from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib import messages
from .models import Exhibitions
from .forms import ExhibitionForm
import datetime


def exhibitions_list(request):
    """ exhibitions display view """
    exhibitions_info = Exhibitions.objects.all()
    for exhibition in exhibitions_info:
        exhibition.now_showing_calc()
        exhibition.save()
    context = {
        'exhibitions': exhibitions_info
    }
    return render(request, 'exhibitions/exhibitions.html', context)


class AddExhibition(View):
    """ A view to return the all_products page """
    def get(self, request):
        """ get request """
        if not request.user.is_superuser:
            messages.error(request,
                           "You are not authorised to view that page.")
            return redirect(reverse('home'))
        else:
            add_exhibition_form = ExhibitionForm()
            return render(request, 'exhibitions/add_exhibition.html',
                          {'add_exhibition_form': add_exhibition_form, })
