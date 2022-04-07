from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


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