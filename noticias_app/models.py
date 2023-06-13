from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)