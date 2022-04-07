from django.shortcuts import render, redirect, reverse, get_object_or_404
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


class EditExhibition(View):
    """ A view to return the edit_product page """
    def get(self, request, pk):
        """ get request """
        if not request.user.is_superuser:
            messages.error(request,
                           "You are not authorised to view that page.")
            return redirect(reverse('home'))
        else:
            exhibition = get_object_or_404(Exhibitions, pk=pk)
            edit_exhibition_form = ExhibitionForm(instance=exhibition)
            return render(request, 'exhibitions/edit_exhibition.html',
                          {'edit_exhibition_form': edit_exhibition_form,
                           'exhibition': exhibition})

    def post(self, request, pk, *args, **kwargs):
        """ post view """
        exhibition = get_object_or_404(Exhibitions, pk=pk)
        form = ExhibitionForm(request.POST, instance=exhibition)
        print(form)
        if form.has_changed():
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
                print(exhibition)
                # save exhibition
                exhibition.save()
                messages.success(
                    request, f"success, {exhibition.name} has been updated.")
                return redirect(reverse('exhibitions_list'), kwargs={'not_shopping': True})
            else:
                print(form.errors.as_data())
                form = ExhibitionForm(instance=exhibition)
                messages.warning(request, "something went wrong...")
                return redirect(
                    reverse('edit_exhibition', args=[exhibition.pk]), kwargs={'not_shopping': True})
        else:
            messages.info(request, "No information has changed.")
            return redirect(reverse('exhibitions_list'), kwargs={'not_shopping': True})


class DeleteExhibition(View):
    """ deleting exhibition """
    def get(self, request, pk):
        """ get request """
        if not request.user.is_superuser:
            messages.error(request,
                           "You are not authorised to view that page.")
            return redirect(reverse('home'))
        else:
            exhibition = get_object_or_404(Exhibitions, pk=pk)
            return render(request, 'exhibitions/delete_exhibition.html',
                          {'exhibition': exhibition})
    def post(self, request, pk, *args, **kwargs):
        """ post view """
        exhibition = get_object_or_404(Exhibitions, pk=pk)
        exhibition.delete()
        messages.success(
            request, f"success, {exhibition.name} has been deleted.")
        return redirect(
            reverse('exhibitions_list'), kwargs={'not_shopping': True})
