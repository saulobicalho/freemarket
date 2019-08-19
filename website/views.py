from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from helloworld.models import Produto
from website.forms import InsereProdutoForm


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

class ProdutoListView(ListView):
    template_name = "website/lista.html"
    model = Produto
    context_object_name = "produtos"


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

class ProdutoCreateView(CreateView):
    template_name = "website/cria.html"
    model = Produto
    form_class = InsereProdutoForm
    success_url = reverse_lazy("website:lista_produtos")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class ProdutoUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Produto
    fields = '__all__'
    context_object_name = 'produto'
    success_url = reverse_lazy("website:lista_produtos")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class ProdutoDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Produto
    fields = '__all__'
    context_object_name = 'produto'
    success_url = reverse_lazy("website:lista_produtos")
