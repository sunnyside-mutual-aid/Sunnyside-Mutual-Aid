from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('martor/', include('martor.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('website.urls')),
)
