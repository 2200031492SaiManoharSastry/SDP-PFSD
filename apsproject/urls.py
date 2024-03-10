"""
URL configuration for apsproject project.

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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home",views.homefunction,name="home"),
    path("login", views.loginfunction, name="login"),
    path("contactus", views.contactfunction, name="contact"),
    path("services", views.servicesfunction, name="services"),
    path("about", views.aboutfunction, name="about"),
    path("dailyhoroscope",views.dailyhoroscope,name="dailyhoroscope"),
    path("horoscope",views.horoscope,name="horoscope"),
     path('forget',views.forget,name="forget"),
     path('nakshatra', views.nakshatra, name='nakshatra'),
    path('input1', views.input1, name='input1'),
     



    path("",include("adminapp.urls")),
    #path("",include("userapp.urls")),
]

