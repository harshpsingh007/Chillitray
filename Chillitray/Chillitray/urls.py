"""Chillitray URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(("mainapp.urls","mainapp"),namespace="mainapp")),
    path('', include("django.contrib.auth.urls")),
    path('api/', include(("mainapp.api.urls","api"),namespace="api")),
    path('task2', include(("task2.urls","task2"),namespace="task2")),
    path('task2/task2api/', include(("task2.task2api.urls","task2api"),namespace="task2API")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
