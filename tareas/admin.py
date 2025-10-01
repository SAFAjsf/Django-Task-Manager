from django.contrib import admin
from .models import Tarea
# Register your models here.
#clase para configurar el administrador.
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'prioridad', 'vigente', 'fecha_limite', 'fecha_creacion')
    list_filter = ('vigente', 'prioridad', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')
#registrar el modelo con su configuracion.
admin.site.register(Tarea, TareaAdmin)