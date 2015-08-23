__author__ = 'dean'

class Map(object):
    scenes = {
        'start': Outside(),
        'hall': Hall(),
        'redDoor': Trap(),
        'greyDoor': Monster(),
        'yellowDoor': Treasure(),
        'death': Death(),
        'victory': Victory()
    }