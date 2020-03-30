from django.conf import settings
from django.contrib import admin
from django.urls import path, include
import statements.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('steps/', include('steps.urls')),
    path('statements/', include('statements.urls')),
    path('blockchain/', include('blockchain.urls')),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
