from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib import messages
from .models import Exhibitions
from .forms import ExhibitionForm
import datetime


def exhibitions_list(request):
    """ exhibitions display view """
    exhibitions_info = Exhibitions.objects.all().order_by('date_starting')
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
                          
    def post(self, request, *args, **kwargs):
        """ post view """
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            exhibition = form.save(commit=False)
            # retrieve dates from post data 
            exhibition_start_date = request.POST.get('date_starting')
            exhibition_end_date = request.POST.get('date_finishing')
            # convert dates to format required by django
            exhibition.date_starting = datetime.datetime.strptime(
                exhibition_start_date, "%d/%m/%Y").date()
            exhibition.date_finishing = datetime.datetime.strptime(
                exhibition_end_date, "%d/%m/%Y").date()
            # work out the status
            exhibition.now_showing_calc()
            # save exhibition
            exhibition.save()
            messages.success(
                request, f"success, {exhibition.name} has been added.")
            return redirect(
                reverse('exhibitions_list'), kwargs={'not_shopping': True})
        else:
            messages.error(request, "something went wrong...")
            return redirect(
                reverse('add_exhibition'), kwargs={'not_shopping': True})

