from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=64)
    health = models.IntegerField()
    attack = models.IntegerField()
    defence = models.IntegerField()
    gold = models.IntegerField()
    location_id = models.IntegerField()

    def location(this):
        return Room.objects.get(id=this.location_id)


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
