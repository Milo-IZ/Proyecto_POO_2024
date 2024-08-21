#-*- coding: utf-8 -*-

from django.db import models

class Materia(models.Model):
    class Meta:
        pass

    int id = None
    int año = None
    str nombre = None


    def agregar_contenido(self, Contenido contenido):
        pass

