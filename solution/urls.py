from django.contrib import admin
from django.urls import path, include

from ticker.urls import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ticker/', include(urlpatterns))
]
