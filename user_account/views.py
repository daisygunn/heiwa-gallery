from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.conf import settings


class UserProfile(View):
    """ view to display user profile """
    def get(self, request):
        """ get request """
        if request.user.is_authenticated:
            user = request.user
            return render(
                request, 'user_account/user_profile.html')
        else:
            messages.warning(
                request, "You must be logged in to view this page.")
            return redirect('home')
