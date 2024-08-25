from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
MATERIA_CHOICES = [
    ("Programacion 2", "PROGRAMACION 2"),
    ("Algoritmos y estructura de Datos", "ALGORITMOS Y ESTRUCTURA DE DATOS"),
    ("Base de Datos 1", "BASE DE DATOS 1"),
    ("Base de Datos 2", "BASE DE DATOS 2"),
    ("Programacion Orientada a Objetos", "PROGRAMACION ORIENTADA A OBJETOS"),
    ("Sistemas Operativos 1", "SISTEMAS OPERATIVOS 1"),
    ("Sistemas Operativos 2", "SISTEMAS OPERATIVOS 2"),
    ("Lenjuajes de Programacion", "LENGUAJES DE PROGRAMACION"),
    ("Electronica", "ELECTRONICA"),
    ("Circuitos Electricos", "CIRCUITOS ELECTRICOS"),
]
# años iren de 1 a 5
ANO_CHOICES = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]


class Contenido(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    contenido = RichTextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    imagen = models.URLField()
    ano = models.TextField(max_length=2, choices=ANO_CHOICES)
    materia = models.CharField(max_length=100, choices=MATERIA_CHOICES)

    def __str__(self):
        return self.materia

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.user.username}'
    
class Denuncia(models.Model):
    DENUNCIA_CHOICES = [("Contenido Inapropiado", "CONTENIDO INAPROPIADO"), ("Contenido Falso", "CONTENIDO FALSO"), ("Contenido Incompleto", "CONTENIDO INCOMPLETO"),("plagio", "PLAGIO"), ("Otro", "OTRO")]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    motivo= models.TextField(max_length=30, choices=DENUNCIA_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Denuncia by {self.user.username} Motivo: {self.motivo}'