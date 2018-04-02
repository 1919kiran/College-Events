from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Create your views here.
def event_index(request):
    events = Event.objects.all()
    return render(request, 'events_index.html', {'events':events})

def event_detail(request, slug):
    events = Event.objects.all()

    existence = 0
    for event in events:
        if slug == event.event_url:
            existence = 1
            event = Event.objects.get(event_url=slug)
            return render(request, 'event_fullview.html', {'event':event})
        else:
            existence = 0

    if existence == 0:
        return render(request, '404.html')
