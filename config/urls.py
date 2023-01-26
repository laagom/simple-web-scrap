from django.contrib import admin
from django.urls import path

from scrap.views import scrap_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scrap_view)
]
