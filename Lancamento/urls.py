"""
URL configuration for Lancamento project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.views.generic import RedirectView

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='menu/')),
    path('menu/', views.menu),
    path('/', views.menu),
    path('login/', views.view_login),
    path('login/submit', views.submitLogin),
    path('submit/', views.submitLogin),
    path('menu/pedidos/', views.pedidos),
    path('menu/produtos', views.produtos),
    path('menu/pedidos/produts', views.produtos)
]
#https://chatgpt.com/share/3f498b25-4bd8-42e2-a259-42c6d192843a