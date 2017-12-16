# Create a Pirate class. While you can add other fields and methods, you must have these methods:-

# drink_some_rum() - intoxicates the Pirate some
# hows_it_going_mate() - when called, the Pirate replies, if drink_some_run was called:-
# 0 to 4 times, "Pour me anudder!"
# else, "Arghh, I'ma Pirate. How d'ya d'ink its goin?", the pirate passes out and sleeps it off.
# If you manage to get this far, then you can try to do the following.

# die() - this kills off the pirate, in which case, drinkSomeRum, etc. just result in he's dead.
# brawl(x) - where pirate fights another pirate (if that other pirate is alive) and there's a 1/3 chance, 1 dies,
# the other dies or they both pass out.
# And... if you get that far...

# Add a parrot.

import random

class Pirate(object):

    def __init__(self):
        self.consumed_rum = 0
        self.alive = True
        self.passed_out = False
    
    def pass_out(self):
        self.passed_out = True
    
    def drink_some_rum(self):
        if self.alive:
            self.consumed_rum += 1
        else:
            print("The pirate is dead.")
    
    def hows_it_going_mate(self):
        if self.alive:
            if self.consumed_rum < 5:
                print("Pour me anudder!")
                self.drink_some_rum()
            else:
                print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
                self.pass_out()
                self.consumed_rum = 0
        else:
            print("The pirate is dead.")

    def die(self):
        self.alive = False
    
    def brawl(self, pirate):
        if isinstance(pirate, Pirate) and pirate.alive:
            chance = random.randint(1, 3)
            if chance == 1:
                self.die()
            elif chance == 2:
                pirate.die()
            else:
                self.pass_out()
                pirate.pass_out()
    
    def __str__(self):
        return ("The pirate is " + ("alive" + " and " + ("passed out." if self.passed_out else "conscious.") if self.alive else "dead."))
