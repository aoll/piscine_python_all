"""d05 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ex01?/', include('ex01.urls')),
    url(r'^ex02?/', include('ex02.urls')),
    url(r'^ex03?/', include('ex03.urls')),
    url(r'^ex04?/', include('ex04.urls')),
    url(r'^ex05?/', include('ex05.urls')),
    url(r'^ex06?/', include('ex06.urls')),
    url(r'^ex07?/', include('ex07.urls')),
    url(r'^ex08?/', include('ex08.urls')),
]
