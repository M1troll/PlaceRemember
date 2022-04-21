from django.urls import path

from . import views


app_name = 'impression_storage'
urlpatterns = [
    path('', views.index, name='index'),
    path('storage/', views.storage, name='storage'),
]
