"""myproject URL Configuration

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
from django.urls import path
from django.conf.urls import url
from myapp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'home/$',home),
    url(r'base/$',base),
    url(r'fruits/$',fruits),
    url(r'apple/$',apple),
    url(r'grapes/$',grapes),
    url(r'orange/$',orange),
    url(r'strawberry/$',strawberry),
    url(r'vegitable/$',vegitable),
    url(r'carrot/$',carrot),
    url(r'potatto/$',potatto),
    url(r'tomatto/$',tomatto),
    url(r'bitter_gourd/$',bitter_gourd),
    url(r'electronics/$',electronics),
    url(r'tv/$',tv),
    url(r'mobile/$',mobile),
    url(r'washingmechine/$',washingmechine),
    url(r'fridge/$',fridge),
    url(r'grocery/$',grocery),
    url(r'atta/$',atta),
    url(r'maida/$',maida),
    url(r'rice/$',rice),
    url(r'oil/$',oil),
    url(r'login/$',login),
    url(r'registration/$',registration),
]
