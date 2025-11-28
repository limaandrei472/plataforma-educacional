from django.contrib import admin
from .models import Usuario, Materia, Assunto

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'tipo_usuario', 'criado_em')
    search_fields = ('nome', 'email')
    ordering = ('nome',)

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    ordering = ('nome',)

@admin.register(Assunto)
class AssuntoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'materia', 'autor', 'atualizado_em')
    list_filter = ('materia', 'autor')
    search_fields = ('titulo',)
    ordering = ('titulo',)