"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from drf_spectacular.utils import extend_schema


@extend_schema(exclude=True)
class SchemaView(SpectacularAPIView):
    pass


urlpatterns = [
    path('admin/', admin.site.urls),
    path('songs/', include('songs.urls')),
    path('schema/', SchemaView.as_view(), name='schema'),
    path('docs/', SpectacularRedocView.as_view(url_name='schema')),
]
