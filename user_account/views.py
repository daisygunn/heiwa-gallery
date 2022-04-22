from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import UserProfile, UserWishlist
from .forms import UserProfileForm
from products.models import Product


def account_overview(request):
    """ show account overview page """
    # if not superuser redirect home
    if not request.user.is_authenticated:
        messages.warning(
            request, "You must be logged in to view this page.")
        return redirect('home')
    # else get user instance
    user = UserProfile.objects.get(user=request.user)
    context = {
                'not_shopping': True,
                'user': user,
            }
    return render(request, 'user_account/account_overview.html', context)


def user_profile_display(request):
    """ view to display user profile """
    # get user instance
    user = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        # if post request fill form with user details from POST
        user_profile_form = UserProfileForm(data=request.POST, instance=user)
        if user_profile_form.is_valid():
            # if the form has changed
            if user_profile_form.has_changed():
                # save the form
                user_profile_form.save()
                messages.success(
                    request, f"Thank you {user.full_name}, "
                    "your information has been updated.")
            else:
                # if no info has changed
                messages.info(
                    request, "No information has been changed.")
        else:
            # if the form isn't valid
            messages.error(
                    request, "Something is not right with your form, "
                    " please check the information provided.")
    else:
        # if user is authenticated
        if request.user.is_authenticated:
            user_profile_form = UserProfileForm(instance=user)
        else:
            # if not redirect back to home page
            messages.warning(
                request, "You must be logged in to view this page.")
            return redirect('home')
    context = {
                'form': user_profile_form,
                'not_shopping': True,
            }
    return render(request, 'user_account/user_profile.html', context)


def user_orders(request):
    """ view to display orders to user """
    user = UserProfile.objects.get(user=request.user)
    # get all orders under user name
    orders = user.orders.all()
    context = {
                'orders': orders,
                'not_shopping': True,
            }
    return render(request, 'user_account/user_orders.html', context)


def add_to_wishlist(request, pk):
    """ view to display orders to user """
    if request.user.is_authenticated:
        # if user is authenticated
        user = UserProfile.objects.get(user=request.user)
        product = get_object_or_404(Product, pk=pk)
        # if the user has any items in their wishlist then remove it
        if UserWishlist.objects.filter(user=user, product=product).exists():
            wishlist_item = UserWishlist.objects.get(
                user=user, product=product)
            wishlist_item.delete()
            messages.info(request, "removed from wishlist")
            return redirect(reverse(
                'all_products'), kwargs={'not_shopping': True})
        else:
            # if the item is not in the wishlist then add it
            wishlist_item = UserWishlist.objects.create(
                user=user, product=product)
            messages.success(request, f"{wishlist_item} added to wishlist")
            return redirect(
                reverse('all_products'), kwargs={'not_shopping': True})
    else:
        # redirect back to all products if the user isn't logged in
        messages.error(request, "You must be logged in to create a wishlist.")
        return redirect(reverse('all_products'), kwargs={'not_shopping': True})


def remove_from_wishlist(request, pk):
    """ view to display orders to user """
    # if user is authenticated
    if request.user.is_authenticated:
        # get user instance
        user = UserProfile.objects.get(user=request.user)
        # get product using pk
        product = get_object_or_404(Product, pk=pk)
        # get wishlist item using user & product
        wishlist_item = UserWishlist.objects.get(user=user, product=product)
        # delete item from wishlist
        wishlist_item.delete()
        messages.info(request, f"{product.name} removed from wishlist")
        return redirect(reverse('wishlist'), kwargs={'not_shopping': True})
    else:
        # if not logged in redirect back to all products
        messages.error(request, "You must be logged in to edit a wishlist.")
        return redirect(reverse('all_products'), kwargs={'not_shopping': True})


def user_wishlist(request):
    """ display wishlist """
    if request.user.is_authenticated:
        # if user is logged in show wishlist
        return render(request, 'user_account/wishlist.html')
    else:
        # if not logged in redirect to home
        messages.error(request, "You must be logged in to view a wishlist.")
        return redirect('home')
