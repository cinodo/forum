from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Topico, Mensagem
from .forms import MensagemForm, RespostaForm

# Create your views here.
class ForumIndex(ListView):
    model = Topico
    paginate_by = 5    
    template_name = 'index.html'

class ForumView(DetailView):
    
    model = Topico
    template_name = 'mensagens.html'
    
    def get_context_data(self,**kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['form'] = MensagemForm(self.request.POST or None)
        return context
    
    def post(self, request, *args, **Kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object = self.object )
        form = context['form']
        if form.is_valid():
            mensagem = form.save(commit = False)
            mensagem.topico = self.object
            mensagem.save()
            messages.success(
                request, 'A sua mensagem foi enviada com sucesso'
            )
            context['form'] = MensagemForm()          
        return self.render_to_response(context)

class MensagemView(DetailView):
    
    model = Mensagem
    template_name = 'respostas.html'
    
    def get_context_data(self,**kwargs):
        context = super(MensagemView, self).get_context_data(**kwargs)
        context['form'] = RespostaForm(self.request.POST or None)
        return context
    
    def post(self, request, *args, **Kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object = self.object )
        form = context['form']
        if form.is_valid():
            resposta = form.save(commit = False)
            resposta.mensagem = self.object
            resposta.save()
            messages.success(
                request, 'A sua resposta foi enviada com sucesso'
            )
            context['form'] = RespostaForm()          
        return self.render_to_response(context)
    
index = ForumIndex.as_view()
topico = ForumView.as_view()
mensagem = MensagemView.as_view()