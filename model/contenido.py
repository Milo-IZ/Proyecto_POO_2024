#-*- coding: utf-8 -*-

from django.db import models

class Contenido(models.Model):
    class Meta:
        pass

    str titulo = None
    str correo_usurio = None
    str contraseña = None
    Usuario autor = None
    str descripcion = None
    Materia materia = None
    int año = None
    Date fecha_publicacion = None
    str contenido = None
    str fuentes = None


    def votar(self, ):
        pass

    def denunciar(self, ):
        pass

    def aprobar(self, ):
        pass

    def publicar contenido(self, ):
        pass

