"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:   path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:    path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:   path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from countries import views
from countries.views import country_create, country_list, country_update, country_delete, country_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first, name='first'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('apidata/', views.countries, name='countries_data'),
    path('countries/', views.country_list, name='country_list'),
    path('countries/new/', views.country_create, name='country_create'),
    path('countries/<int:pk>/edit/', views.country_update, name='country_update'),
    path('countries/<int:pk>/delete/', views.country_delete, name='country_delete'),
]
