"""Diploma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

#import views from Pages>views:
from Pages.views import fortigate_view, base_view, home_view, configure_view, copy_view, about_view


#our group of views linked to relative url paths:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fortigate/', fortigate_view),
    path('', home_view),
    path('base/',base_view),
    path('configure', configure_view()),
    path('copy', copy_view()),
    path('about', about_view())
]
