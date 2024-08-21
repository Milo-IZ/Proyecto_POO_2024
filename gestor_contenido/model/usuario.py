#-*- coding: utf-8 -*-

import sqlite3
import bcrypt
from django.db import models

class Usuario(models.Model):
    class Meta:
        pass

    correo_usurio = models.CharField(max_length=255)
    psswd = models.CharField(max_length=255)
    rol = models.CharField(max_length=255)


    def abrir_base_datos(self):
        sqlite3.connect('usuarios.db')
        pass
        

    def registrar(self):
        pass

    def iniciar_sesion(self):
        pass

    def is_admin(self):
        pass

    def menu_admin(self):
        pass

    def menu_usuario(self, correo_usuario, psswd):
        while True:
            print("\n--- Inicio de Sesion ---")
            correo_usuario = input("1. Ingrese su Correo:")
            psswd=input("2. Ingrese su Contraseña")
            
    