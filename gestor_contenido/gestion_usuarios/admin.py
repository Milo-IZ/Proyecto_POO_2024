from django.contrib import admin

# Register your models here.
from .models import Usuario 
from .models import Materia
from .models import Contenido
from .models import Votar
from .models import Denuncia
from .models import Comentarios

admin.site.register(Usuario)
admin.site.register(Materia)
admin.site.register(Contenido)
admin.site.register(Votar)
admin.site.register(Denuncia)
admin.site.register(Comentarios)
