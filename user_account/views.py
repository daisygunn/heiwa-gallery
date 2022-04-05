from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import View


class UserProfile(View):
    """ view to display user profile """
    def get(self, request):
        """ get request """
        return render(
            request, 'user_account/user_profile.html')
