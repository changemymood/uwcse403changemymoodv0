'''
Created on Oct 5, 2012

@author: hunlan
'''
from django.shortcuts import render_to_response
from django.http import HttpResponse
from somedata.models import Characters

def storeData_form(request):
    return render_to_response('testing.html');

def storeData(request):    
    # if character is in request
    if 'character' in request.GET:
        user_input = request.GET['character']
        if user_input.strip() == '':
            return HttpResponse('cannot input empty string')
        
        try:
            Characters.objects.get(chars=user_input)
        except Characters.DoesNotExist:
            Characters.objects.create(chars=user_input)
            return HttpResponse('Added ' + user_input + ' to Database')
        else:
            return HttpResponse('Already in Database')
    else:
        return HttpResponse('You submitted an empty form.')

def displayData(request):
    arr = Characters.objects.all()
    msg = ''
    for ch in arr:
        msg += ch.chars + '<br>'
    return HttpResponse(msg)

def clearData(request):
    Characters.objects.all().delete()
    return HttpResponse('cleared database')