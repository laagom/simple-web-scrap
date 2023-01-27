from django.urls import path

from scrap.views import scrap_view, index

urlpatterns = [
    path('', index),
    path('scrap/', scrap_view),
]