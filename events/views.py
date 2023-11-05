from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from django.views.generic import *

def HomePage(request,id):
    response = 'hello from %s'
    return HttpResponse(response % id)
def eventStatic(req):
    list =[
       {
            'title':'title1',
            'description' : 'description1'
        },
        {
            'title':'title2',
            'description' : 'description2'
        }
    ]
    return render(req,'events/staticList.html',{'events':list})

def EventList(request):
    list=Event.objects.all()
    print(list)
    return render(request,'events/EventList.html',{'events':list})

class EventListClass(ListView):
    model=Event
    template_name= 'events/EventListView.html'
    context_object_name='events'
    
# Create your views here.
