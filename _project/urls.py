from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    # custom
    path("", include("apps.main.urls")),
    path("aida/", include("apps.aida.urls")),
]
