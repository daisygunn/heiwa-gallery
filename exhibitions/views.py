from django.shortcuts import render

# Create your views here.
def exhibitions(request):
    """ exhibitions display view """
    return render(request, 'exhibitions/exhibitions.html')