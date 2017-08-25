from django.contrib import admin
from .models import Topico, Mensagem, Resposta

# Register your models here.
class TopicoAdmin(admin.ModelAdmin):
    
    list_display = ['titulo']
    prepopulated_fields = {'slug' : ('titulo',)}
    
    
class MensagemAdmin(admin.ModelAdmin):
    
    list_display = ['autor','texto']   
    
class RespostaAdmin(admin.ModelAdmin):
    
    list_display = ['autor','texto']


admin.site.register(Topico, TopicoAdmin)
admin.site.register(Mensagem, MensagemAdmin)
admin.site.register(Resposta, RespostaAdmin)