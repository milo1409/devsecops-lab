from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def health(_request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("", include("django_prometheus.urls")),  # expone /metrics
    path("health", health),
]
