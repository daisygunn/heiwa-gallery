from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """
    return render(request, 'home/about.html')


def error_404(request, exception):
    """ 404 error page """
    return render(request, 'home/404.html', status=404)


def error_500(request):
    """ 500 error page """
    return render(request, 'home/500.html', status=500)
