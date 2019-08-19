from website.views import IndexTemplateView, ProdutoListView, ProdutoUpdateView, ProdutoCreateView, \
    ProdutoDeleteView

from django.urls import path

app_name = 'website'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /produto/cadastrar
    path('produto/cadastrar', ProdutoCreateView.as_view(), name="cadastra_produto"),

    # GET /produtos
    path('produtos/', ProdutoListView.as_view(), name="lista_produtos"),

    # GET/POST /produto/{pk}
    path('produto/<pk>', ProdutoUpdateView.as_view(), name="atualiza_produto"),

    # GET/POST /produtos/excluir/{pk}
    path('produto/excluir/<pk>', ProdutoDeleteView.as_view(), name="deleta_produto"),
]
