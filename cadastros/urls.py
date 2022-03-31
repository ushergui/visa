from django.urls import path #Estou pegando do módulo django


from .views import EstadoCreate, CidadeCreate, BairroCreate, LogradouroCreate, \
    ProprietarioCreate, TerrenoCreate, ProtocoloCreate, FiscalCreate, InspecaoCreate, InfracaoCreate, DefesaCreate, ReinspecaoCreate

from .views import EstadoUpdate, CidadeUpdate, BairroUpdate, LogradouroUpdate, \
    ProprietarioUpdate, TerrenoUpdate, ProtocoloUpdate, FiscalUpdate, InspecaoUpdate, InfracaoUpdate, DefesaUpdate, ReinspecaoUpdate, ARCreate, DefesasCreate, ReinspecoesCreate, ARJulgamento

from .views import EstadoDelete, CidadeDelete, BairroDelete, LogradouroDelete, \
    ProprietarioDelete, TerrenoDelete, ProtocoloDelete, FiscalDelete, InspecaoDelete, InfracaoDelete, DefesaDelete, ReinspecaoDelete

from .views import EstadoList, CidadeList, BairroList, LogradouroList, \
    ProprietarioList, TerrenoList, ProtocoloList, FiscalList, InspecaoList, InfracaoList, InfracaoList2, InformacoesList, ReinspecaoList, ProdutividadeList, GerenciarList

from .views import gerar_relatorio, gerar_ar1, gerar_ar2, gerar_auto, gerar_ar3, gerar_ar4, gerar_ar5, gerar_ar6, gerar_manifestacao, gerar_julgamento

from . import views

#padrão de url que tem lá na outra url, ele funciona como se fosse um vetor

urlpatterns = [
    #path('cadastrar/produtividade/', ProdutividadeCreate.as_view(), name="cadastrar-produtividade"),
    path('cadastrar/estado/', EstadoCreate.as_view(), name="cadastrar-estado"),
    path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('cadastrar/bairro/', BairroCreate.as_view(), name="cadastrar-bairro"),
    path('cadastrar/logradouro/', LogradouroCreate.as_view(), name="cadastrar-logradouro"),
    path('cadastrar/proprietario/', ProprietarioCreate.as_view(), name="cadastrar-proprietario"),
    path('cadastrar/terreno/', TerrenoCreate.as_view(), name="cadastrar-terreno"),
    path('cadastrar/protocolo/', ProtocoloCreate.as_view(), name="cadastrar-protocolo"),
    path('cadastrar/fiscal/', FiscalCreate.as_view(), name="cadastrar-fiscal"),
    path('cadastrar/inspecao/', InspecaoCreate.as_view(), name="cadastrar-inspecao"),
    path('cadastrar/infracao/', InfracaoCreate.as_view(), name="cadastrar-infracao"),
    path('cadastrar/defesa/', DefesaCreate.as_view(), name="cadastrar-defesa"),
    path('cadastrar/reinspecao/', ReinspecaoCreate.as_view(), name="cadastrar-reinspecao"),
    #Para edição é necessário colocar o ID

   # path('editar/produtividade/<int:pk>/', ProdutividadeUpdate.as_view(), name="editar-produtividade"),
    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
    path('editar/bairro/<int:pk>/', BairroUpdate.as_view(), name="editar-bairro"),
    path('editar/logradouro/<int:pk>/', LogradouroUpdate.as_view(), name="editar-logradouro"),
    path('editar/proprietario/<int:pk>/', ProprietarioUpdate.as_view(), name="editar-proprietario"),
    path('editar/terreno/<int:pk>/', TerrenoUpdate.as_view(), name="editar-terreno"),
    path('editar/protocolo/<int:pk>/', ProtocoloUpdate.as_view(), name="editar-protocolo"),
    path('editar/fiscal/<int:pk>/', FiscalUpdate.as_view(), name="editar-fiscal"),
    path('editar/inspecao/<int:pk>/', InspecaoUpdate.as_view(), name="editar-inspecao"),
    path('editar/infracao/<int:pk>/', InfracaoUpdate.as_view(), name="editar-infracao"),
    path('editar/defesa/<int:pk>/', DefesaUpdate.as_view(), name="editar-defesa"),
    path('editar/reinspecao/<int:pk>/', ReinspecaoUpdate.as_view(), name="editar-reinspecao"),
    path('cadastrar/AR/<int:pk>/', ARCreate.as_view(), name="cadastrar-AR"),
    path('cadastrar/defesa/<int:pk>/', DefesasCreate.as_view(), name="cadastrar-defesa"),
    path('cadastrar/defesa/<int:pk>/', DefesasCreate.as_view(), name="cadastrar-defesa"),
    path('cadastrar/reinspecao/<int:pk>/', ReinspecoesCreate.as_view(), name="cadastrar-reinspecao"),
    path('cadastrar/AR2/<int:pk>/', ARJulgamento.as_view(), name="cadastrar-AR2"),

    # Para deletar é necessário colocar o ID

    #path('deletar/produtividade/<int:pk>/', ProdutividadeDelete.as_view(), name="deletar-produtividade"),
    path('deletar/estado/<int:pk>/', EstadoDelete.as_view(), name="deletar-estado"),
    path('deletar/cidade/<int:pk>/', CidadeDelete.as_view(), name="deletar-cidade"),
    path('deletar/bairro/<int:pk>/', BairroDelete.as_view(), name="deletar-bairro"),
    path('deletar/logradouro/<int:pk>/', LogradouroDelete.as_view(), name="deletar-logradouro"),
    path('deletar/proprietario/<int:pk>/', ProprietarioDelete.as_view(), name="deletar-proprietario"),
    path('deletar/terreno/<int:pk>/', TerrenoDelete.as_view(), name="deletar-terreno"),
    path('deletar/protocolo/<int:pk>/', ProtocoloDelete.as_view(), name="deletar-protocolo"),
    path('deletar/fiscal/<int:pk>/', FiscalDelete.as_view(), name="deletar-fiscal"),
    path('deletar/inspecao/<int:pk>/', InspecaoDelete.as_view(), name="deletar-inspecao"),
    path('deletar/infracao/<int:pk>/', InfracaoDelete.as_view(), name="deletar-infracao"),
    path('deletar/defesa/<int:pk>/', DefesaDelete.as_view(), name="deletar-defesa"),
    path('deletar/reinspecao/<int:pk>/', ReinspecaoDelete.as_view(), name="deletar-reinspecao"),


    # Para listar
    #path('listar-produtividade/', ProdutividadeList.as_view(), name="listar-produtividade"),
    path('listar-estados/', EstadoList.as_view(), name="listar-estados"),
    path('listar-cidades/', CidadeList.as_view(), name="listar-cidades"),
    path('listar-bairros/', BairroList.as_view(), name="listar-bairros"),
    path('listar-logradouros/', LogradouroList.as_view(), name="listar-logradouros"),
    path('listar-proprietarios/', ProprietarioList.as_view(), name="listar-proprietarios"),
    path('listar-terrenos/', TerrenoList.as_view(), name="listar-terrenos"),
    path('listar-protocolos/', ProtocoloList.as_view(), name="listar-protocolos"),
    path('listar-fiscais/', FiscalList.as_view(), name="listar-fiscais"),
    path('listar-inspecoes/', InspecaoList.as_view(), name="listar-inspecoes"),
    path('listar-infracoes/', InfracaoList.as_view(), name="listar-infracoes"),
    path('listar-produtividades/', ProdutividadeList.as_view(), name="listar-produtividades"),
    path('listar-informacoes/', InformacoesList.as_view(), name="listar-informacoes"),
    path('gerenciar-infracoes/', GerenciarList.as_view(), name="gerenciar-infracoes"),
    path('gerenciar-defesas/', InfracaoList2.as_view(), name="gerenciar-defesas"),
    path('listar-reinspecoes/', ReinspecaoList.as_view(), name="listar-reinspecoes"),



    # Para gerar
    path('gerar_relatorio/<int:pk>/', gerar_relatorio, name='gerar_relatorio'),
    path('gerar_ar1/<int:pk>/', gerar_ar1, name='gerar_ar1'),
    path('gerar_ar2/<int:pk>/', gerar_ar2, name='gerar_ar2'),
    path('gerar_ar3/<int:pk>/', gerar_ar3, name='gerar_ar3'),
    path('gerar_ar4/<int:pk>/', gerar_ar4, name='gerar_ar4'),
    path('gerar_ar5/<int:pk>/', gerar_ar5, name='gerar_ar5'),
    path('gerar_ar6/<int:pk>/', gerar_ar6, name='gerar_ar6'),
    path('gerar_auto/<int:pk>/', gerar_auto, name='gerar_auto'),
    path('gerar_manifestacao/<int:pk>/', gerar_manifestacao, name='gerar_manifestacao'),
    path('gerar_julgamento/<int:pk>/', gerar_julgamento, name='gerar_julgamento'),



]

