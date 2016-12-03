from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('maze/index.html')
    context = {
        'room': {
            'name': 'Room 1',
        },
        'player': {
            'status': [
                { 'name': 'HP', 'val': 3 },
                { 'name': 'ATK', 'val': 1 },
            ]
        }
    }
    return HttpResponse(template.render(context, request))
