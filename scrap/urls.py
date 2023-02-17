from django.urls import path

from scrap.views import index, scrap_view

urlpatterns = [
    path('', index),
    path('scrap/', scrap_view),
]