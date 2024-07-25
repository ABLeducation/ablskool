"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('users.urls', 'users'), namespace='users')),
    path('users/', include('django.contrib.auth.urls')),
    path('curriculum/', include(('curriculum.urls','curriculum'), namespace='curriculum')),
    path('mechanzo/', include(('mechanzo.urls','mechanzo'),namespace="mechanzo")),
    # path('accounts/', include('allauth.urls')),
    path('api/', include('api.urls')),
    path('assessment/', include(('assessment.urls', 'assessment'), namespace='assessment')),
    path('ebook/', include(('ebook.urls', 'ebook'), namespace='ebook')),
    path('silk/', include('silk.urls', namespace='silk'))
]

urlpatterns += [path('i18n/', include('django.conf.urls.i18n'))]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)