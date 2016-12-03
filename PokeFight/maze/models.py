from django.db import models

# models that are FIXED for fun.
class Player:
    def __init__(this):
        this.status = {
            'HP': 10,
            'ATK': 1,
            'DEF': 0,
        }
        this.items = {
        }

class Room:
    def __init__(this, roomname = "default"):
        this.name = roomname







# Create your models here.
