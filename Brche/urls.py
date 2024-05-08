"""
URL configuration for Brche project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.frontpage, name='header'),
    path("login.html/", views.login, name='login'),
    path("A01.html/", views.A01, name='A01'),
    path("A02.html/", views.A02, name='A02'),

]
