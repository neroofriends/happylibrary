"""
URL configuration for nerooMovies project.

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
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload_, name='upload'),
    path('upload/', views.upload_, name='upload/'),
    path('search', views.search, name="search"),
    path('register', views.registerer, name='register'),
    path('login', views.login_, name='login'),
    path('logout', views.logout_, name='logout'),
    path('about', views.about_, name="about"),
    path('account', views.account_, name="account"),
    path('download/<int:pk>', views.download, name='download'),
]

urlpatterns += staticfiles_urlpatterns()
