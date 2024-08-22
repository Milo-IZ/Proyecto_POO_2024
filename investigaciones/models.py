from django.db import models

# Create your models here.

class Contenido(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor= models.CharField(max_length=100)
    imagen = models.URLField()
    
    

    def __str__(self):
        return self.titulo
