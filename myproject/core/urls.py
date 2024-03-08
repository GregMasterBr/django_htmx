from django.urls import path
from  . import views, htmx_views

urlpatterns = [
    path('', views.home, name='home'),
    path('listar_produtos/', views.listar_produtos, name='listar_produtos'),

]

htmx_urlpatterns = [
    path('checar_produto/', htmx_views.checar_produto, name='checar_produto'),
    path('salvar_produto/', htmx_views.salvar_produto, name='salvar_produto'),
    path('deletar_produto/<int:id>', htmx_views.deletar_produto, name='deletar_produto'),
]

urlpatterns+= htmx_urlpatterns