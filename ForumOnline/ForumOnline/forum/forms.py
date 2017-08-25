from django import forms

from .models import Mensagem, Resposta

class MensagemForm(forms.ModelForm):
    
    class Meta:
        model = Mensagem
        fields = ['autor','texto']

        
class RespostaForm(forms.ModelForm):
    
    class Meta:
        model = Resposta
        fields = ['autor','texto']