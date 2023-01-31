from django.urls import path

from scrap.views import wwr_crap_view, idd_crap_view, index

urlpatterns = [
    path('', index),
    path('scrap/wwr/', wwr_crap_view),
    path('scrap/idd/', idd_crap_view),
]