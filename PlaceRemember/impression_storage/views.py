from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import View

from .models import Impression, Profile


class Index(View):
    context = {}

    def get(self, request):
        return render(request, 'impression_storage/index.html', self.context)


class Storage(View):
    context = {}

    def get(self, request):
        self.context["impressions"] = Impression.objects.filter(author=request.user)
        return render(request, 'impression_storage/storage.html', self.context)
