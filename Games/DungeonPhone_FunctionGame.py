## For Chapter 45 in Python3 the Hard Way book

from sys import exit
from random import randint
from textwrap import dedent
import time

# Player is an adventurer who forgot their phone in the last dungeon.
# This is their quest to get the phone back.

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene!
        current_scene.enter()


class Death(Scene):

    sarcastic_exit = [
        "Oh wow.  You're dead."
        "Well, that didn't last long.  You are dead."
        "You totes die!"
        "Epic fail."
        "[insert yo momma joke]"
    ]

    def enter(self):
        print(Death.sarcastic_exit[randint(0, len(self.sarcastic_exit)-1)])

# Where you get the premise of what you're doing etc.
class Intro(Scene):

    def enter(self):
        print(dedent("""
        skldjflsjfsl
        sldkfjdslkfjsdlfj
        ksdjhfkjsdhfksd
        """))

    action = input("> ")

    # if-then loops here for outcomes


# You'll have to get past this area in order to
# get into the area with the dragon.
class TestHall(Scene):

    def enter(self):
        print(dedent("""
        skldjflsjfsl
        sldkfjdslkfjsdlfj
        ksdjhfkjsdhfksd
        """))

# The dragon is sad.
class SadDragon(Scene):

    def enter(self):
        print(dedent("""
        skldjflsjfsl
        sldkfjdslkfjsdlfj
        ksdjhfkjsdhfksd
        """))

# And now the dragon is MAD!
class MadDragon(Scene):

    def enter(self):
        print(dedent("""
        skldjflsjfsl
        sldkfjdslkfjsdlfj
        ksdjhfkjsdhfksd
        """))

# This one is where you've found your phone and
# the DM starts yelling at you using random words.
class PhoneFound(Scene):

    def enter(self):
        print(dedent("""
        What in the %%% are you %%%???  Do I always
        have to %%% in your %%% for you to %%% that
        this is a CRAFT, and it takes %%%, and %%%, and
        time, you ungrateful %%%!!!!!!
        """))

class Finished(Scene):

    def enter(self):
        print(dedent("""
        Your DM is frothing at the mouth now, but at
        least you've found your phone!  Congrats!
        """))
        return 'finished'

class Map(object):

    scenes = {
        'intro': Intro(),
        'test_hall': TestHall(),
        'sad_dragon': SadDragon(),
        'mad_dragon': MadDragon(),
        'phone_found': PhoneFound(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('intro')
a_game = Engine(a_map)
a_game.play()
