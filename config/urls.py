from django.contrib import admin
from django.urls import include, path

from scrap.views import scrap_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scrap.urls'))
]
