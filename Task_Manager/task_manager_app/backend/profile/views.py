# profile/views.py

from django.shortcuts import render
from django.views import View

class ProfileView(View):
    def get(self, request):
        return render(request, 'profile/profile.html')

