#-*- coding: utf-8 -*-

from django.db import models

class Usuario(models.Model):
    class Meta:
        pass

    str correo_usurio = None
    str Contraseña = None
    str rol = None


    def registrar(self, ):
        pass

    def iniciar sesion(self, ):
        pass

    def is_admin(self, ):
        pass

    def menu_admin(self, ):
        pass

