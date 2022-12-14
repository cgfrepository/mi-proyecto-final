"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ejemplo.views import (index,index2,index3,imc,
                           monstrar_familiares, BuscarFamiliar,AltaFamiliar)
from blog.views import index as blog_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar/<nombre>/<apellido>/', index2),
    path('mostrar-notas', index3),
    path('imc/<peso>/<altura>/', imc),
    path('mi-familia/', monstrar_familiares),
    path('blog/', blog_index), #sSe menciona que no funciona esta linea, pero si lo hace sino no mostraria el template avanzado.
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
]

