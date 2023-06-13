Proyecto Django - Sitio de noticias
Este proyecto Django es una página de noticias desarrollada utilizando el patrón MVT (Modelo-Vista-Plantilla). 
Proporciona funcionalidades básicas como agregar noticias, buscar en la base de datos y visualizar las noticias existentes

Funcionalidades implementadas:
- Herencia de HTML: La plantilla base "base.html" es heredada por las demás plantillas para compartir la estructura común de la página.
- Clases en models.py_ con una estrucura basica orientadas a un sitio de noticias.
- Formularios para buscar datos en forms.py

Estructura del Proyecto
- proyecto_noticias/: Carpeta main del proyecto Django.
- proyecto_noticias/proyecto_noticias: contiene el archivo de configuración principal y otros archivos de configuración del proyecto.
 - settings.py: Archivo de configuración del proyecto Django.
 - urls.py: Archivo de configuración de URL del proyecto.
 - wsgi.py: Archivo de configuración para el servidor web.
 - noticias_app/: Carpeta de la aplicación Django.
 - migrations/: Carpeta que contiene los archivos de migración.
 - templates/: Carpeta que contiene las plantillas HTML de la aplicación.
 - forms.py: Archivo donde se definen los formularios de la aplicación.
 - models.py: Archivo donde se definen los modelos de la aplicación.
 - views.py: Archivo donde se definen las vistas de la aplicación.
- manage.py: Archivo utilizado para realizar tareas relacionadas con el proyecto Django.
- README.txt: Este archivo que proporciona instrucciones y descripción del proyecto.
