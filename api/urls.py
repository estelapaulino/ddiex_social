from django.conf.urls.defaults import *
from piston.resource import Resource
from ddiex_social.api.handlers import BolsistaHandler, AjudaCustoHandler, EditalHandler

bolsista_handler = Resource(BolsistaHandler)

ajuda_handler = Resource(AjudaCustoHandler)

edital_handler = Resource(EditalHandler)


urlpatterns = patterns('',
   url(r'^bolsista/(?P<bolsista_id>[^/]+)/', bolsista_handler, { 'emitter_format': 'json' }),
   url(r'^bolsistas/', bolsista_handler, { 'emitter_format': 'json' }),
   url(r'^ajuda_custo/(?P<ajuda_id>[^/]+)/', ajuda_handler, { 'emitter_format': 'json' }),
   url(r'^lista_ajuda/', ajuda_handler, { 'emitter_format': 'json' }),   
   url(r'^edital/', edital_handler, { 'emitter_format': 'json' }),
)
