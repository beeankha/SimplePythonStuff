## For Chapter 45 in Python3 the Hard Way book

import random
import time

from random import randint
from sys import exit
from textwrap import dedent


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
        "Oh wow.  You're dead. \n",
        "Well, that didn't last long.  You are dead. \n",
        "You totes die! \n",
        "EPIC FAIL. \n",
        "[insert yo momma joke].  Aaaaaand you're dead. \n"
    ]

    def enter(self):
        print(Death.sarcastic_exit[randint(0, len(self.sarcastic_exit)-1)])

        time.sleep(2)
        print("Do you want to play again? (yes or no)")
        playAgain = input("> ")

        if playAgain == 'yes' or playAgain == 'y':
            return 'intro'
        else:
            exit(1)


class Intro(Scene):

    def enter(self):
        print(dedent("""
            You are the type of person who goes out and about questing in various
            caves and dungeons and whatnot.  One day, while questing in such a manner,
            you leave a dungeon only to realize that you've forgotten your phone inside.
            """))

        time.sleep(1)
# AFTER GAME IS FINALIZED, TURN THE ABOVE INTO 6

        print("Drat!")

        time.sleep(1)

        print(dedent("""
            That thing isn't cheap, so you turn around and go straight back in the
            last cave you came out of.  You have a really bad memory, so you are a bit
            surprised to see that there are three doors ahead of you, each in a different
            color.  One is blue, one is yellow, and another is purple.  Which do you choose?

            Type in your choice, 'yellow', 'blue', or 'purple'.
            """))

        door_choice = input("> ")

        if door_choice == "yellow":
            print(dedent("""
                You open the yellow door and step into the room like you own the
                place. Problem is, you shoulda seen that instead of a floor there
                is a bottomless pit, which you promptly plunge into. \n \n
                """))
            return 'death'

        elif door_choice == "blue":
            print(dedent("""
                Blue is nice, blue is calming!  You open the door and step into
                the room. You walk a few steps forward, only to hear the door slam
                behind you. \n \n
                """))

            time.sleep(4)

            print("You're trapped! \n \n")

            time.sleep(2)

            print("Like, seriously, you're trapped here. \n \n")

            time.sleep(1.5)

            print("Forever. \n \n")

            time.sleep(1.5)

            print("There's no getting out. \n \n")

            time.sleep(1.5)

            return 'death'

        elif door_choice == "purple":
            print(dedent("""
                Your memory may be bad, but you are a smart one.  You chose the
                non-primary color door!  High fives all around!

                You open the door and enter a cold, large, musty hall with a long table
                in it. \n \n
                """))
            return 'test_hall'

        else:
            print("DOES NOT COMPUTE!")
            return 'intro'


# # You'll have to get past this area in order to
# # get into the area with the dragon.
class TestHall(Scene):

    def enter(self):
        print(dedent("""
            Around the table are many chairs. Seated in one of them is a what
            appears to be a goblin. It starts talking to you in a really posh
            British accent and asks you to pass the 'Flerzlum'. What is he talking
            about? You try to follow his gaze and see three things he could be
            asking for. One is a plate of rocks. Another is a bowl of soup with
            eyeballs floating in it. There is also a silver pitcher. Which do
            you hand him?
            """))

        time.sleep(1)
# AFTER GAME IS FINALIZED, TURN THE ABOVE INTO 6

        print("Pass the 'rocks', 'soup' or 'pitcher'?")
        print("You can also 'pass' and not give him anything. \n \n")

        goblin_pass = input("> ")

        if goblin_pass == "pass":
            print(dedent("""
                Yikes, the goblin REALLY doesn't like that! He takes his
                sword out and stabs you with it. \n
                """))
            return 'death'

        if goblin_pass == "rocks":
            print(dedent("""
                The goblin looks at you like you are an insane person, takes out
                his sword, and stabs you with it. \n
                """))
            return 'death'

        if goblin_pass == "pitcher":
            print(dedent('''
                The goblin angrily grabs the pitcher from you and yells "This is
                not flerzlum, you big stupid idiot!" and throws it really hard
                at your head. The last thing you hear is your skull cracking. \n
                '''))
            return 'death'

        elif goblin_pass == "soup":
            print(dedent('''
                The goblin gratefully accepts the bowl of soup and slurps it all
                down. He says "Thank you for your assistance! In return, I will
                allow you to pass without kill you! At the end of this hall is
                another door. Behind it, you will find a dragon. Be cautious,
                for this dragon has a bad temper!" \n
                '''))
            return 'sad_dragon'

        else:
            print("DOES NOT COMPUTE!")
            return 'test_hall'


# The dragon is sad.
class SadDragon(Scene):

    def enter(self):
        print(dedent("""
            You walk through the door at the end of the hall as instructed and
            enter what looks like a cave lined with gold. There is treasure filling
            the entire place all the way up to the ceiling, which is so high the
            torchlight all around can't reach it.
            """))

        time.sleep(1.5)

        print("In the midst of the treasure is a dragon.  It's big.  And it's crying.")

        time.sleep(1.5)

        print(dedent('''
            You go up to the dragon and ask what's wrong.  The dragon answers through
            tears, "I'm SO sad! Nobody comes to visit me here! Even when they DO visit,
            they all leave in such a hurry! Look, someone left their phone here!"
            You look at where the dragon is pointing and indeed see your phone!
            Politely, you ask if you can have the phone back.  In response, the dragon
            says, "Wait. Did YOU leave it here? Hmph. How rude of you to not stay longer
            the last time you were here! How are you gonna make up for it?"
            '''))

        time.sleep(1.5)

        print(dedent('''
            Well, this is quite a pickle. You can maybe sing to it, go up and give
            it a hug, or cross your arms and say "Nothin'!".
            '''))

        print("Choose 'sing', 'hug' or 'nothing'.")

        dragon_choice = input("> ")

        if dragon_choice == "sing":
            print(dedent("""
                [sing death text here]
                """))
            return 'death'

        if dragon_choice == "hug":
            print(dedent(f"""
                [mad dragon text here]
                """))
            return 'mad_dragon'

        if dragon_choice == "nothing":
            print(dedent("""
                [defiant death text]
                """))
            return 'death'

        else:
            print("DOES NOT COMPUTE!")
            return 'sad_dragon'


# And now the dragon is MAD!
class MadDragon(Scene):

    def enter(self):
        print(dedent("""
            [secret code needed oh yeah, dragon gives clue]
            """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        cheat = "4242"
        guess = input("[phone password?]> ")
        guesses = 0

        while guess != code and guess != cheat and guesses < 9:
            print("Try again!")
            guesses += 1
            guess = input("[phone password?]> ")

        if guess == cheat:
            print(dedent("""
                [right answer text]
                """))
            return 'phone_found'

        elif guess == code:
            print(dedent("""
                Holy crap!  You got it!
                """))
            return 'phone_found'

        else:
            print(dedent("""
                You have used up all of your unlock tries and your phone is locked
                up for the next five minutes, aside from emergency calls.  Dialing
                911 will do you no good, however, as the dragon eats you. \n
                """))
            return 'death'


# This one is where you've found your phone and
# the DM starts yelling at you using random words.
class PhoneFound(Scene):

    with open("words.txt") as f:
        lines = [line.strip() for line in f]
    # This makes lines a class attribute in PhoneFound!!
    # .strip() method will remove extraneous stuff like whitespace etc.


    def enter(self):
        # sample() method included in random library
        # https://docs.python.org/3/library/random.html#random.sample

        # condense the below part!! Maybe try random.sample
        madwords = random.sample(self.lines, 8)

        print(dedent(f'''
            Woah, your DM is mad. He starts yelling at you in words that make
            no sense:
            "What in the {madwords[0]} are you {madwords[1]}???  Do I always
            have to {madwords[2]} in your {madwords[3]} for you to {madwords[4]} that
            this is a CRAFT, and it takes {madwords[5]}, and {madwords[6]}, and
            time, you ungrateful {madwords[7]}!!!!!!"
            '''))

        return 'finished'


class Finished(Scene):

    def enter(self):
        print(dedent("""
            Your DM is frothing at the mouth now, but at
            least you've found your phone!  Congrats!
            """))

        time.sleep(2)


# Troubleshoot this part!!
        print("Do you want to play again? (yes or no)")
        play_again = input("> ")

        another_round1 = 'yes'
        another_round2 = 'y'

        if play_again == another_round1:
            return 'intro'
        elif play_again == another_round2:
            return 'intro'
        else:
            exit(1)


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
