from django.shortcuts import render
from .models import Exhibitions


def exhibitions_list(request):
    """ exhibitions display view """
    exhibitions_info = Exhibitions.objects.all()
    for exhibition in exhibitions_info:
        exhibition.now_showing_calc()
    context = {
        'exhibitions': exhibitions_info
    }
    return render(request, 'exhibitions/exhibitions.html', context)
