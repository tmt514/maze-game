from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import *

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
    # 取得monster
    monsters = room.monster_set.all()

    ### 第二步：根據目前的指令執行對應動作
    q = request.GET.get('q', None)
    if q == None:
        pass
    else:
        cmd, param = q.split(":")
        if cmd == "goto":
            roomid = int(param)
            msg.append("依依不捨地離開了 <strong>" + room.name + "</strong>!")
            room = Room.objects.get(id=roomid)
            player.location_id = roomid
            player.save()
            msg.append("移動到 <strong>" + room.name + "</strong>!")
        elif cmd == "use":
            pi = PlayerItem.objects.get(id=int(param))
            if pi.item.name == 'banana':
                player.attack += 3
                player.save(update_fields=['attack'])
                pi.delete()
        elif cmd == "attack":
            mon = Monster.objects.get(id=int(param))
            msg.append("對 <strong>" + mon.name + "</strong> 造成了<strong>" + str(player.attack) + "</strong>傷害，效果卓著!")
            mon.health -= player.attack
            mon.save(update_fields=['health'])


    # 判斷是不是新的地點
    if player.playerroom_set.filter(room=room).exists() == False:
        new_playerroom = PlayerRoom(room=room, player=player)
        new_playerroom.save()
        msg.append("探索了新的地點 <strong>" + room.name + "</strong>!")
        # TODO: 獲得道具
        room_items = room.roomitem_set.all()
        for ri in room_items:
            msg.append("獲得"+ri.item.name+": "+ri.item.info)
            pi = PlayerItem(item=ri.item, player=player)
            pi.save()



    template = loader.get_template('maze/index.html')
    context = {
        'msg': msg,
        'room': room,
        'player': player,
        'monsters': monsters,
    }
    return HttpResponse(template.render(context, request))
