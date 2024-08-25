from django.contrib import admin

# Register your models here.
from .models import Contenido, Comment, Denuncia, Voto

admin.site.register(Contenido)
admin.site.register(Comment)
admin.site.register(Denuncia)
admin.site.register(Voto)

