from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Impression
from .forms import ImpressionForm


class IndexView(View):
    context = {}

    def get(self, request):
        return render(request, 'impression_storage/index.html', self.context)


class StorageView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = '/'

    context = {
        'form': ImpressionForm(),
    }

    def get(self, request):
        self.context["impressions"] = Impression.objects.filter(author=request.user)
        return render(request, 'impression_storage/storage.html', self.context)

    @staticmethod
    def post(request):
        form = ImpressionForm(request.POST)
        if form.is_valid():
            impression = form.save(commit=False)
            impression.author = request.user
            impression.save()

        return redirect('/storage/')


class EditStorageView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = '/'

    context = {}

    def get(self, request, pk):
        try:
            impression = Impression.objects.get(pk=pk)

            # Check the deletion
            if impression.is_deleted:
                return redirect('/storage/')

        except Impression.DoesNotExist:
            return render(request, 'impression_storage/storage.html', self.context)

        self.context["impression_pk"] = impression.pk
        self.context["form"] = ImpressionForm(instance=impression)

        return render(request, 'impression_storage/edit_storage.html', self.context)

    def post(self, request, pk):
        try:
            impression = Impression.objects.get(pk=pk)
        except Impression.DoesNotExist:
            return render(request, 'impression_storage/storage.html', self.context)

        form = ImpressionForm(request.POST, request.FILES)
        if form.is_valid():
            for key, value in form.cleaned_data.items():
                setattr(impression, key, value)
            impression.save()

        return redirect('/storage/')


class DeleteImpressionView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = '/'

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
