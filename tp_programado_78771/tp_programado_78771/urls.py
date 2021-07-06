"""tp_programado_78771 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from ejercicio253 import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('ejercicio253/', views.simulacion.as_view())
]

#from django.urls import path, include
#from . import views
#from .runge_kutta import runge_kutta_desgaste,runge_kutta_limpieza

#urlpatterns = [
#    path('ejercicio57/', views.simulacion.as_view()),
#    path('runge_kutta/', runge_kutta_desgaste.simulacion.as_view()),
#    path('runge_kutta_limpieza/', runge_kutta_limpieza.simulacion.as_view())
#]