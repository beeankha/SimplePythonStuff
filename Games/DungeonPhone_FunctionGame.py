## For Chapter 45 in Python3 the Hard Way book

from sys import exit
from random import randint
from textwrap import dedent
import time

# Player is an adventurer who forgot their phone in latest dungeon.
# This is their quest to get the phone back.

class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class Intro(Scene):

    def enter(self):
        pass

class TestHall(Scene):

    def enter(self):
        pass

class SadDragon(Scene):

    def enter(self):
        pass

class PhoneFound(Scene):

    def enter(self):
        pass


class Map(object):

    scenes = {
        'intro': Intro(),
        'test_hall': TestHall(),
        'sad_dragon': SadDragon(),
        'phone_found': PhoneFound(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
