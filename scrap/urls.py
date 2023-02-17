from django.urls import path

from scrap.views import index, scrap_view, export_view

urlpatterns = [
    path('', index),
    path('scrap/', scrap_view),
    path('export/', export_view),
]