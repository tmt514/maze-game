from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Player, Room

def index(request):
    player_id = request.session.get('player_id', None)

    # 取得玩家物件
    if player_id == None:
        # 初始化新的玩家
        player = Player(name="新玩家", health=10, attack=0, defence=0, gold=0)
        player.location_id = Room.objects.first().id
        player.save()
        player_id = player.id
    else:
        player = Player.objects.get(id=player_id)
        # TODO: handle exception

    # 取得地點物件
    room = player.location()

    template = loader.get_template('maze/index.html')
    context = {
        'room': room,
        'player': player,
    }
    return HttpResponse(template.render(context, request))
