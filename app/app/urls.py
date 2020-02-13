"""app URL Configuration"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

admin.site.site_header = 'Mea'
admin.site.index_title = 'Mea'
admin.site.site_title = 'Mea'
admin.site.site_url = ''

urlpatterns = [
	url(r'^jet/', include('jet.urls', 'jet')),
	path('admin/', admin.site.urls),
	path('accounts/', include('django.contrib.auth.urls')),
	path('api/users/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
