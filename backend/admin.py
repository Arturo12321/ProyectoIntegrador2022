from django.contrib import admin
from .models import Dispositivo,Alerta,Usuario 
# Register your models here.

class DispositivoAdmin(admin.ModelAdmin):
    list_display=("id","estudiante","dni")
    search_fields=("id","estudiante","dni",)
    list_filter=("id","estudiante","dni")

class AlertaAdmin(admin.ModelAdmin):
    list_display = ("id","fecha","iddispositivo")
    search_fields = ("id","fecha","iddispositivo",)
    list_filter = ("id","fecha","iddispositivo")

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id","apellido","nombre","dni","correo","iddispositivo")
    search_field = ("id","apellido","nombre","dni","correo","iddispositivo",)
    list_filter = ("id","apellido","nombre","dni","correo","iddispositivo")

admin.site.register(Dispositivo,DispositivoAdmin)
admin.site.register(Alerta,AlertaAdmin)
admin.site.register(Usuario,UsuarioAdmin)
