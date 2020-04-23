from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from website.views import admin_uploader

urlpatterns = [
    path('admin/', admin.site.urls),
    path('martor/', include('martor.urls')),
    path('api/uploader/', admin_uploader, name='markdown_uploader_page'),
]

urlpatterns += i18n_patterns(
    path('', include('website.urls')),
)
