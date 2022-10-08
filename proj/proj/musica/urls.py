from django.urls import include, path
from . import views

from django.urls import include, path
from . import views

app_name = 'musica'
urlpatterns = [

  path("", views.index, name="index"),
  path('logout', views.logoutview, name = 'logout'),
  path('registar', views.registar, name = 'registar'),
  path('entrar', views.entrar, name = 'entrar'),
  path('registration', views.registration, name = 'registration'),


  path("inicio", views.inicio, name="inicio"),


  path('social', views.social, name="social"),
  path('social/<int:post_id>', views.detalhe, name='detalhe'),
  path('social/<int:post_id>/gosto', views.like, name='gosto'),
  path('social/novopost', views.novopost, name='novopost'),
  path('social/<int:user_id>/adicionarpost', views.adicionarpost, name='adicionarpost'),
  path('social/<int:post_id>/novocomentario', views.novocomentario, name='novocomentario'),
  path('social/<int:post_id>/adicionarcomentario', views.adicionarcomentario, name='adicionarcomentario'),
  path('social/<int:post_id>/apagarpost', views.apagarpost, name= 'apagarpost'),


  path('centro_ajuda', views.centro_ajuda, name="centro_ajuda"),
  path('centro_ajuda/procura', views.procura, name="procura"),
  path('centro_ajuda/procura/novopedido', views.novopedido, name="novopedido"),
  path('centro_ajuda/procura/<int:user_id>/publicar_procura', views.publicar_procura, name="publicar_procura"),
  path('centro_ajuda/procura/<int:pedido_id>', views.detalhe_ajuda, name='detalhe_ajuda'),
  path('centro_ajuda/<int:pedido_id>/apagarajuda', views.apagarajuda, name= 'apagarajuda'),

  path('centro_ajuda/oferta', views.oferta, name="oferta"),
  path('centro_ajuda/oferta/novaoferta', views.novaoferta, name="novaoferta"),
  path('centro_ajuda/oferta/<int:user_id>/publicar_oferta', views.publicar_oferta, name="publicar_oferta"),
  path('centro_ajuda/oferta/<int:oferta_id>', views.detalhe_oferta, name='detalhe_oferta'),
  path('centro_ajuda/<int:oferta_id>/apagaroferta', views.apagaroferta, name= 'apagaroferta'),


  path('projetos', views.projetos, name = "projetos"),
  path('projetos/novoproj', views.novoproj, name = 'novoproj'),
  path('projetos/<int:user_id>/publicar_proj', views.publicar_proj, name = "publicar_proj"),
  path('projetos/<int:proj_id>', views.detalhe_projeto, name = 'detalhe_projeto'),
  path('projetos/<int:proj_id>/apagarprojeto', views.apagarprojeto, name = 'apagarprojeto'),


  path('venda', views.venda, name = "venda"),
  path('venda/novavenda', views.novavenda, name = 'novavenda'),
  path('venda/<int:user_id>/publicar_venda', views.publicar_venda, name = "publicar_venda"),
  path('venda/<int:venda_id>', views.detalhe_venda, name = 'detalhe_venda'),
  path('venda/<int:venda_id>/apagarvenda', views.apagarvenda, name = 'apagarvenda'),


  path('aboutUs', views.aboutUs, name = "aboutUs"),

]
