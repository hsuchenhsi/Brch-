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
    path("describe.html/", views.describe, name='describe'),
    path("A02.html/", views.A02, name='A02'),
    path("order.html/", views.order, name='order'),
    path("information.html/", views.information, name='order'),
    path("user_login/", views.user_login, name='user_login'),
    path("member.html/", views.member, name='member'),
    path('manage_products.html/', views.manage_products, name='manage_products'),
    path('delete/<str:productNo>/', views.delete_product, name='delete_product'),
    path('edit/<str:productNo>/', views.edit_product, name='edit_product'),
    path('upload.html/', views.upload_file, name='upload_file'),


]
