#-*- coding: utf-8 -*-

from django.db import models

class Contenido(models.Model):
    class Meta:
        pass

    str titulo 
    str correo_usurio
    str contraseña
    Usuario autor
    str descripcion
    Materia materia 
    int año 
    Date fecha_publicacion = None
    str contenido
    str fuentes 


    def votar(self, ):
        pass

    def denunciar(self, ):
        pass

    def aprobar(self, ):
        pass

    def publicar_contenido(self, ):
        pass

