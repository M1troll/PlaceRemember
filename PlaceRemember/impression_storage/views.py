from django.shortcuts import render


def index(request):
    context = {}

    return render(request, 'impression_storage/index.html', context)