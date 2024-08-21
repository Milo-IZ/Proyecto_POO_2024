#-*- coding: utf-8 -*-

from django.db import models

class Votar(models.Model):
    class Meta:
        pass

    int contador = None
    Contenido contenido = None
    Usuario usuario = None
    bool valido = None


    def registrar_voto(self, ):
        pass

