from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=64)
    health = models.IntegerField()
    attack = models.IntegerField()
    defence = models.IntegerField()
    gold = models.IntegerField()
    location_id = models.IntegerField()

    def location(self):
        return Room.objects.get(id=self.location_id)

    class Action:
        name = ""
        key = ""
        def __init__(self, name="", key=""):
            self.name = name
            self.key = key

    def get_actions(self):
        ret = []

        # 獲得 Room Actions
        room = self.location()
        for x in room.neighbors.all():
            ret.append(self.Action(name = "前往 " + x.name, key = "goto:" + str(x.id)))

        # 獲得 Item Actions
        items = this.playeritem_set
        #for i in items:
        #    ret.append(this.Action(name = "使用 " + i.item.name, key = "use:" + str(i.item.id)))
        # 獲得 Monster Actions

        return ret


class Room(models.Model):
    name = models.CharField(max_length=64)
    info = models.TextField()
    image_url = models.TextField()

    neighbors = models.ManyToManyField("self")

class Item(models.Model):
    name = models.CharField(max_length=64)
    info = models.TextField()

class RoomItem(models.Model):
    # the item appears in each room
    item = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE,
        null=True
    )
    room = models.ForeignKey(
        'Room',
        on_delete=models.CASCADE,
        null=True
    )
    number = models.IntegerField()

class PlayerRoom(models.Model):
    room = models.ForeignKey(
        'Room',
        on_delete=models.CASCADE,
    )
    player = models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
    )

class PlayerItem(models.Model):
    item = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE,
    )
    player = models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
    )

class Monster(models.Model):
    pass







# Create your models here.
