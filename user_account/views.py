from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.views import View
from django.contrib import messages
from .models import UserProfile, UserWishlist
from .forms import UserProfileForm
from products.models import Product


def account_overview(request):
    """ show account overview page """
    if not request.user.is_authenticated:
        messages.warning(
            request, "You must be logged in to view this page.")
        return redirect('home')
    user = UserProfile.objects.get(user=request.user)
    context = {
                'not_shopping': True,
            }
    return render(request, 'user_account/account_overview.html', context)


def user_profile_display(request):
    """ view to display user profile """
    user = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        user_profile_form = UserProfileForm(data=request.POST, instance=user)
        if user_profile_form.is_valid():
            if user_profile_form.has_changed():
                user_profile_form.save()
                messages.success(
                    request, f"Thank you {user.full_name}, "
                    "your information has been updated.")
            else:
                messages.info(
                    request, "No information has been changed.")
        else:
            messages.error(
                    request, "Something is not right with your form, "
                    " please check the information provided.")
    else:
        if request.user.is_authenticated:
            user_profile_form = UserProfileForm(instance=user)
        else:
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
    print(user)
    orders = user.orders.all()
    context = {
                'orders': orders,
                'not_shopping': True,
            }
    return render(request, 'user_account/user_orders.html', context)


def add_to_wishlist(request, pk):
    """ view to display orders to user """
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        product = get_object_or_404(Product, pk=pk)
        if UserWishlist.objects.filter(user=user, product=product).exists():
            wishlist_item = UserWishlist.objects.get(user=user, product=product)
            wishlist_item.delete()
            messages.info(request, "removed from wishlist")
            return redirect(reverse('all_products'), kwargs={'not_shopping': True})
        else:
            wishlist_item = UserWishlist.objects.create(user=user, product=product)
            messages.success(request, f"{wishlist_item} added to wishlist")
            return redirect(reverse('all_products'), kwargs={'not_shopping': True})
    else:
        messages.error(request, "You must be logged in to create a wishlist.")
        return redirect(reverse('all_products'), kwargs={'not_shopping': True})

def remove_from_wishlist(request, pk):
    """ view to display orders to user """
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        product = get_object_or_404(Product, pk=pk)
        wishlist_item = UserWishlist.objects.get(user=user, product=product)
        wishlist_item.delete()
        messages.info(request, "removed from wishlist")
        return redirect(reverse('wishlist'), kwargs={'not_shopping': True})
    else:
        messages.error(request, "You must be logged in to edit a wishlist.")
        return redirect(reverse('all_products'), kwargs={'not_shopping': True})

def user_wishlist(request):
    """ display wishlist """
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        list_to_display = []
        for item in UserWishlist.objects.filter(user=user):
            list_to_display.append(item.product)
        print(list_to_display)
        # products = Product.objects.filter(product_wishlist=request.user)
        context = {
            'wishlist_items': list_to_display,
        }
        return render(request, 'user_account/wishlist.html', context)
    else:
        messages.error(request, "You must be logged in to view a wishlist.")
        return redirect('home')
