from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',


    url(r'^servico/', 'ddiex_social.aplicacao.views.servico', name='servico'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'ddiex_social.aplicacao.views.index', name='index'),
    url(r'^bolsa/', 'ddiex_social.aplicacao.views.bolsa', name='bolsa'),
    url(r'^cadastrar_bolsa/', 'ddiex_social.aplicacao.views.cadastrar_bolsa', name='cadastrar_bolsa'),
    url(r'^editar_bolsa/(?P<codigo>\d+)', 'ddiex_social.aplicacao.views.editar_bolsa', name='editar_bolsa'),
    url(r'^excluir_bolsa/(?P<codigo>\d+)', 'ddiex_social.aplicacao.views.excluir_bolsa', name='excluir_bolsa'),
    
    url(r'^inscricao/(?P<codigo>\d+)', 'ddiex_social.aplicacao.views.inscricao', name='inscricao'),
    
    
    url(r'^edital/', 'ddiex_social.aplicacao.views.edital', name='edital'),
    url(r'^cadastrar_edital/', 'ddiex_social.aplicacao.views.cadastrar_edital', name='cadastrar_edital'),
    url(r'^editar_edital/(?P<codigo>\d+)', 'ddiex_social.aplicacao.views.editar_edital', name='editar_edital'),
    url(r'^excluir_edital/(?P<codigo>\d+)', 'ddiex_social.aplicacao.views.excluir_edital', name='excluir_edital'),
    url(r'^setor/', 'ddiex_social.aplicacao.views.setor', name='setor'),
    url(r'^cadastrar_setor/', 'ddiex_social.aplicacao.views.cadastrar_setor', name='cadastrar_setor'),
    url(r'^editar_setor/(?P<codigo>\d+)', 'ddiex_social.aplicacao.views.editar_setor', name='editar_setor'),
    url(r'^excluir_setor/(?P<codigo>\d+)', 'ddiex_social.aplicacao.views.excluir_setor', name='excluir_setor'),
    url(r'^vincular_setor/', 'ddiex_social.aplicacao.views.vincular_setor', name='vincular_setor'),
    url(r'^ajuda_custo/', 'ddiex_social.aplicacao.views.ajuda_custo', name='ajuda_custo'),
    url(r'^cadastrar_ajuda_custo/', 'ddiex_social.aplicacao.views.cadastrar_ajuda_custo', name='cadastrar_ajuda_custo'),
    url(r'^editar_ajuda_custo/(?P<codigo>\d+)', 'ddiex_social.aplicacao.views.editar_ajuda_custo', name='editar_ajuda_custo'),
    url(r'^excluir_ajuda_custo/(?P<codigo>\d+)', 'ddiex_social.aplicacao.views.excluir_ajuda_custo', name='excluir_ajuda_custo'),
    url(r'^editar_bolsista/(?P<codigo>\d+)', 'ddiex_social.aplicacao.views.editar_bolsista', name='editar_bolsista'),
    url(r'^excluir_bolsista/(?P<codigo>\d+)', 'ddiex_social.aplicacao.views.excluir_bolsista', name='excluir_bolsista'),
    url(r'^cadastrar_bolsista/', 'ddiex_social.aplicacao.views.cadastrar_bolsista', name='cadastrar_bolsista'),
    url(r'^bolsista/', 'ddiex_social.aplicacao.views.bolsista', name='bolsista'),
    url(r'^imprimir/(?P<codigo>\d+)', 'ddiex_social.aplicacao.views.imprimir', name='imprimir'),
    url(r'^editar_bolsista/(?P<codigo>\d+)', 'ddiex_social.aplicacao.views.editar_bolsista', name='editar_bolsista'),
    url(r'^permissao/', 'ddiex_social.aplicacao.views.permissao', name='permissao'),
    url(r'^relatorio/', 'ddiex_social.aplicacao.views.relatorio', name='relatorio'),
    url(r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/', 'django.contrib.auth.views.logout', {'template_name': 'logout.html', 'next_page': '/login'}),
    
)
