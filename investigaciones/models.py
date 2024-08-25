from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
MATERIA_CHOICES = [
    ("IS210", "IS-210"), ("MM110", "MM-110"), ("MM111", "MM-111"),
    ("IS310", "IS-310"), ("IS410", "IS-410"), ("IS411", "IS-411"), 
    ("IS412", "IS-412"), ("IS501", "IS-501"), ("IS510", "IS-510"), 
    ("IS511", "IS-511"), ("IS512", "IS-512"), ("IS513", "IS-513"), 
    ("IS601", "IS-601"), ("IS602", "IS-602"), ("IS603", "IS-603"),
    ("IS611", "IS-611"), ("IS701", "IS-701"), ("IS702", "IS-702"),
    ("IS711", "IS-711"), ("IS721", "IS-721"),("IS802", "IS-802"),
    ("IS811", "IS-811"), ("IS820", "IS-820"), ("IS902", "IS-902"),
    ("IS903", "IS-903"), ("IS904", "IS-904"), ("IS905", "IS-905"),
    ("IS906", "IS-906"), ("IS910", "IS-910"), ("IS911", "IS-911"),
    ("IS912", "IS-912"), ("IS913", "IS-913"), ("IS914", "IS-914"),
]

# años iren de 1 a 5
ANO_CHOICES = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]


class Contenido(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    contenido = models.TextField()
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
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)  # Add this line
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.user.username}'
    
class Denuncia(models.Model):
    DENUNCIA_CHOICES = [("Contenido Inapropiado", "CONTENIDO INAPROPIADO"), ("Contenido Falso", "CONTENIDO FALSO"), ("Contenido Incompleto", "CONTENIDO INCOMPLETO"),("plagio", "PLAGIO"), ("Otro", "OTRO")]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=30, choices=DENUNCIA_CHOICES)  # Changed to CharField
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Denuncia by {self.user.username} Motivo: {self.motivo}'
    
    
class Voto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # Add a rating field
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Voto by {self.user.username} on {self.contenido.titulo}'