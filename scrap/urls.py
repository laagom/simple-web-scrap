from django.urls import path

from scrap.views import scrap_view

urlpatterns = [
    path('', scrap_view)
]