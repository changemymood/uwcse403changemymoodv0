'''
Created on Oct 6, 2012

@author: hunlan
'''
from django.conf.urls import patterns, url
from piston.resource import Resource
from handlers import DatabaseHandler

db_handler = Resource(DatabaseHandler)

urlpatterns = patterns('',
    url(r'^characters/', db_handler),
)