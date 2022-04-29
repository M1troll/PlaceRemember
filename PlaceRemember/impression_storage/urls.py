from django.urls import path, re_path
from django.contrib.auth.views import LogoutView

from .views import *


app_name = 'impression_storage'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('delete/<int:pk>', DeleteImpressionView.as_view(), name='delete_impression'),
    path('storage/', StorageView.as_view(), name='storage'),
    path('storage/<int:pk>/', EditStorageView.as_view(), name='storage_edit'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # re_path(r'^.*', IndexView.as_view(), name='index'),
]
