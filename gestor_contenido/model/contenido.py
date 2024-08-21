#-*- coding: utf-8 -*-

from django.db import models

class Contenido(models.Model):
    class Meta:
        pass

    titulo = None
    correo_usurio = None
    contraseña = None
    autor = None
    descripcion = None
    materia = None
    año = None
    fecha_publicacion = None
    contenido = None
    fuentes = None
    
    
    def votar(self):
        pass
    
    def denunciar(self):
        pass
    
    def aprobar(self):
        pass
    
    def publicar_contenido(self):
        pass

