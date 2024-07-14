from django.contrib import admin
from .models import Contato, Categoria
# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'telefone', 'categoria','mostrar')
    list_display_links = ('nome',)
    list_editable = ('telefone','mostrar',)
    list_per_page = 3


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
