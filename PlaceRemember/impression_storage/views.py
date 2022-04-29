from django.shortcuts import render, redirect
from django.views import View

from .models import Impression
from .forms import ImpressionForm


class IndexView(View):
    context = {}

    def get(self, request):
        return render(request, 'impression_storage/index.html', self.context)


class StorageView(View):
    context = {
        'form': ImpressionForm(),
    }

    def get(self, request, pk=''):
        self.context["impressions"] = Impression.objects.filter(author=request.user)
        return render(request, 'impression_storage/storage.html', self.context)

    @staticmethod
    def post(request, pk=''):
        form = ImpressionForm(request.POST)
        if form.is_valid():
            impression = form.save(commit=False)
            impression.author = request.user
            impression.save()

        return redirect('/storage/')


class DeleteImpressionView(View):
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
