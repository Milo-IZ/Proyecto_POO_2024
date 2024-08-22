from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    ESTUDIANTE = 'estudiante'
    DOCENTE = 'docente'
    ADMINISTRADOR = 'administrador'

    ROLES_CHOICES = [
        (ESTUDIANTE, 'Estudiante'),
        (DOCENTE, 'Docente'),
        (ADMINISTRADOR, 'Administrador'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_usuario = models.EmailField()
    psswd = models.CharField(max_length=255)
    rol = models.CharField(
        max_length=50,
        choices=ROLES_CHOICES,
        default=ESTUDIANTE,
    )
    
    def save(self, *args, **kwargs):
        # Solo encripta la contraseña si no está encriptada ya
        if not self.psswd.startswith('pbkdf2_sha256$'):
            self.psswd = make_password(self.psswd)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # Verifica si la contraseña en texto plano coincide con la encriptada
        return check_password(raw_password, self.psswd)
        
    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
         
class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    año = models.IntegerField()
    nombre = models.CharField(max_length=50)

class Contenido(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.TextField()
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    año = models.IntegerField()
    fecha_publicacion = models.DateField()
    contenido = models.TextField()
    fuentes = models.TextField()
    
class Denuncia(models.Model):
    contador = models.IntegerField()
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    motivo = models.TextField()

class Votar(models.Model):
    contador = models.IntegerField()
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    valido = models.BooleanField()

class Comentarios(models.Model):
    id = models.AutoField(primary_key=True)
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    likes = models.IntegerField()