from django.shortcuts import render
from .models import Exhibitions


def exhibitions_list(request):
    """ exhibitions display view """
    exhibitions_info = Exhibitions.objects.all()
    context = {
        'exhibitions': exhibitions_info
    }
    return render(request, 'exhibitions/exhibitions.html', context)
