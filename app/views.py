from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def Insert_Topic(request):
    tn=input('Enter topic name: ')
    to=Topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()  
    return HttpResponse('data inserted')


def Insert_Website (request):
    tn=input('Enter topic name: ')
    to=Topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()
    n=input('enter name: ')
    u=input('Enter url : ')
    wo=Webpage.objects.get_or_create(Topic_name=to,name=n,url=u)
    wo.save()

    

def Insert_Acces_Records(request):
    pk=int(input('Enter pk hear : '))
    web=Webpage.objects.get(pk=pk)
    web.save()

    
    









    

    


    
    