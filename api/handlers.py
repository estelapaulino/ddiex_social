from piston.handler import AnonymousBaseHandler, BaseHandler
from aplicacao.models import Bolsista, AjudaCusto, Edital, Inscricao

class BolsistaHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Bolsista   

    def read(self, request, bolsista_id=None):
        
        base = Bolsista.objects
        
        if bolsista_id:
            return base.get(pk=bolsista_id)
        else:
            return base.all() 
            


class AjudaCustoHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = AjudaCusto   

    def read(self, request, ajuda_id=None):
        
        base = AjudaCusto.objects
        
        if ajuda_id:
            return base.get(pk=ajuda_id)
        else:
            return base.all() 


class EditalHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Edital   

    def read(self, request):
        
        base = Edital.objects
        
        return base.all() 
        
        

