from django.shortcuts import render, get_object_or_404
from .models import Event

def index(request):
    event_list = Event.objects.all()
    return render(request, 'home/index.html', {'event_list': event_list})

def about(request):
    return render(request, 'home/about.html', {'event_list': event_list})

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'home/detail.html', {'event': event})
