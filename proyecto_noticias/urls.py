from django.contrib import admin
from django.urls import path
from noticias_app.views import index, agregar_noticia, buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('agregar-noticia/', agregar_noticia, name='agregar_noticia'),
    path('buscar/', buscar, name='buscar'),
]