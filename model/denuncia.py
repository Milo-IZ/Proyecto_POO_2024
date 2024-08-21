#-*- coding: utf-8 -*-

from django.db import models

class Denuncia(models.Model):
    class Meta:
        pass

    int contador = None
    Contenido contenido = None
    Usuario usuario = None
    str motivo = None


    def registrar_denuncia(self, ):
        pass

