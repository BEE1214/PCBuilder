"""pcbuilder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from pages.views import home_view,about_view, build_view, profile_view
from components.views import component_view, component_create, dynamic_lookup_view

urlpatterns = [
    path('',home_view, name='home'),
    path('admin/', admin.site.urls),
    path('about/',about_view, name='about'),
    path('build/', build_view, name='build'),
    path('profile/', profile_view, name='profilef'),
    # Components
    path('component/',component_view, name='component'),
    path('component_create/', component_create),
    path('component/<int:aId>/', dynamic_lookup_view, name='component'),

]