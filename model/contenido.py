#-*- coding: utf-8 -*-

from django.db import models

class Contenido(models.Model):
    class Meta:
        pass

    String titulo = None
    String correo_usurio = None
    String contraseña = None
    Usuario autor = None
    String descripcion = None
    Materia materia = None
    int año = None
    Date fecha_publicacion = None
    String contenido = None
    String fuentes = None


    def votar(self, ):
        pass

    def denunciar(self, ):
        pass

    def aprobar(self, ):
        pass

    def publicar contenido(self, ):
        pass

