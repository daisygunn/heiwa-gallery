from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


class UserProfiles(View):
    """ view to display user profile """
    def get(self, request):
        """ get request """
        if request.user.is_authenticated:
            user = UserProfile.objects.get(user=request.user)
            info_form = UserProfileForm(instance=user)
            context = {
                'form': info_form,
                # 'user': user,
            }
            return render(
                request, 'user_account/user_profile.html', context)
        else:
            messages.warning(
                request, "You must be logged in to view this page.")
            return redirect('home')
