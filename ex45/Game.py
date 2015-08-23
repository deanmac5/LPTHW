__author__ = 'dean'

from sys import exit
import Engine
import Map

start = Map('outside')
game = Engine(start)
game.play()