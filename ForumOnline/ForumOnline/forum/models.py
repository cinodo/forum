from django.db import models

# Create your models here.
class Topico(models.Model):
    
    titulo = models.CharField('Titulo', max_length = 100)    
    texto = models.TextField('Texto', max_length = 255)
    slug = models.SlugField('Identificador', max_length = 100, unique = True)
    
    def __str__(self):
        return self.titulo
    
    @models.permalink
    def get_absolute_url(self):
        return ('forum:topico', (), {'slug':self.slug})
    
    class Meta:
        verbose_name = 'Tópico'
        verbose_name_plural = 'Tópicos'
        ordering = ['titulo']
        

class Mensagem(models.Model):
    
    texto = models.TextField('Texto')
    autor = models.CharField('Autor', max_length = 100, blank = True, null= True)
    topico = models.ForeignKey(Topico,
        verbose_name = 'Tópico',
        related_name= 'mensagens',                       
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.texto[:50]
    
    @models.permalink
    def get_absolute_url(self):
        return ('forum:mensagem', (), {'pk':self.pk})
    
    criado = models.DateTimeField('criado', auto_now_add = True)
    
    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
        ordering = ['criado']
    

class Resposta(models.Model):
    
    autor = models.CharField('Autor', max_length = 100, blank = True, null= True)
    texto = models.TextField('Texto')
    mensagem = models.ForeignKey(Mensagem,
        verbose_name = 'Mensagem',
        related_name= 'respostas', 
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.texto[:50]
    
    criado = models.DateTimeField('criado', auto_now_add = True)
    
    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'
        ordering = ['criado']
    