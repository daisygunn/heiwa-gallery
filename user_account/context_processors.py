from .models import UserWishlist, UserProfile


def get_wish_list(request):
    """ get wishlist list to be used across website """
    if request.user.is_authenticated:
        # get user instance
        user = UserProfile.objects.get(user=request.user)
        list_to_display = []
        # if there are items in the users wishlist
        for item in UserWishlist.objects.filter(user=user):
            # append the item to list to display
            list_to_display.append(item.product)
    else:
        # render empty list to not cause issues
        list_to_display = []
    return {
            'wishlist_items': list_to_display,
        }
