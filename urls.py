from django.http import HttpResponse
from django.urls import path


def ads_txt(request):
    continut = "google.com, pub-3528838516008800, DIRECT, f08c47fec8942fa0"
    return HttpResponse(continut, content_type="text/plain")


urlpatterns = [
    # ... rutele tale existente ...
    path("ads.txt", ads_txt),
]
