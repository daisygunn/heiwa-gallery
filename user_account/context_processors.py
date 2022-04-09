from .models import UserWishlist, UserProfile


def get_wish_list(request):
    """ get wishlist list to be used across website """
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        list_to_display = []
        for item in UserWishlist.objects.filter(user=user):
            list_to_display.append(item.product)
        print(list_to_display)
    else:
        list_to_display = []
    return {
            'wishlist_items': list_to_display,
        }
    
