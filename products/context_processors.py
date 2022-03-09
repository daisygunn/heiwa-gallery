from .models import Category


def get_category_list(request):
    """ get category list to be used in navbar """
    category_list = Category.objects.all()
    return {
         'category_list': category_list,
     }
