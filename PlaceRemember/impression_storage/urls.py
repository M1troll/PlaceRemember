from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *


app_name = 'impression_storage'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('add/', AddImpression.as_view(), name='new_impression'),
    path('delete/<int:pk>', DeleteImpression.as_view(), name='delete_impression'),
    path('storage/', Storage.as_view(), name='storage'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
