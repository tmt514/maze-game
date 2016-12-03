from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Player, Room

def index(request):
    # 初始化訊息欄位
    msg = []

    ### 第一步：取得當前狀態
    player_id = request.session.get('player_id', None)

    # 取得玩家物件
    if player_id == None:
        # 初始化新的玩家
        player = Player(name="新玩家", health=10, attack=0, defence=0, gold=0)
        player.location_id = Room.objects.first().id
        player.save()
        player_id = player.id
        request.session['player_id'] = player_id
        msg.append("新玩家誕生了！")
    else:
        player = Player.objects.get(id=player_id)
        # TODO: handle exception

    # 取得地點物件
    room = player.location()
    msg.append("獲得科科")




    ### 第二步：根據目前的指令執行對應動作






    template = loader.get_template('maze/index.html')
    context = {
        'msg': msg,
        'room': room,
        'player': player,
    }
    return HttpResponse(template.render(context, request))
