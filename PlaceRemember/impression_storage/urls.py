from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *


app_name = 'impression_storage'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('storage/', Storage.as_view(), name='storage'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
