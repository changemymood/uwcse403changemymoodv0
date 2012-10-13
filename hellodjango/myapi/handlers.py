'''
Created on Oct 6, 2012

@author: hunlan
'''
from hellodjango.somedata.models import Characters
from piston.handler import BaseHandler

class DatabaseHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Characters
    
    def read(self, request, char_id=None):
        base = Characters.objects
        
        if char_id:
            return base.get(chars=char_id)
        else:
            return base.all()