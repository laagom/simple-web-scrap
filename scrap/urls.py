from django.urls import path

from scrap.views import index, scrap_view, export_view, search_view

urlpatterns = [
    path('', index),
    path('search/', search_view),
    path('scrap/', scrap_view),
    path('export/', export_view),
]