from django.shortcuts import render, redirect
from django.views import View

from .models import Impression


class Index(View):
    context = {}

    def get(self, request):
        return render(request, 'impression_storage/index.html', self.context)


class Storage(View):
    context = {}

    def get(self, request):
        self.context["impressions"] = Impression.objects.filter(author=request.user)
        return render(request, 'impression_storage/storage.html', self.context)


class AddImpression(View):
    context = {}

    def get(self, request):
        return render(request, 'impression_storage/add_impression.html', self.context)

    def post(self, request):
        return render(request, 'impression_storage/storage.html', self.context)


class DeleteImpression(View):
    context = {}

    @staticmethod
    def get(request, pk):
        try:
            i = Impression.objects.get(pk=pk)
            i.is_deleted = True
            i.save()
        except Impression.DoesNotExist:
            pass

        return redirect('/storage/')
