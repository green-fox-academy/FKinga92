# Create a Ship class.
# The Ship stores Pirate-s instances in a list as the crew and has one captain who is also a Pirate.
#   When a ship is created it doesn't have a crew or a captain.
# The ship can be filled with pirates and a captain via fill_ship() method.
#   Filling the ship with a captain and random number of pirates.
# Ships should be represented in a nice way on command line including information about
#   captains consumed rum, state (passed out / died)
#   number of alive pirates in the crew
# Ships should have a method to battle other ships: ship.battle(otherShip)
#   should return true if the actual ship (this) wins
#   the ship should win if its calculated score is higher
#   calculate score: Number of Alive pirates in the crew - Number of consumed rum by the captain
#   The loser crew has a random number of losses (deaths).
#   The winner captain and crew has a party, including a random number of rum :)

import random
from pirate import Pirate

class Ship(object):

    def __init__(self):
        self.crew = []
        self.captain = None

    def fill_ship(self):
        self.captain = Pirate()
        for i in range(random.randint(1, 100)):
            self.crew.append(Pirate())

    def state_of_crew(self):
        number_of_alive_pirates = 0
        for pirate in self.crew:
            if pirate.alive:
                number_of_alive_pirates += 1
        return number_of_alive_pirates

    def get_ship_score(self):
        return self.state_of_crew() - self.captain.consumed_rum

    def battle(self, other_ship):
        if not isinstance(other_ship, Ship):
            return
        if self.get_ship_score() >= other_ship.get_ship_score():
            winner = self
            loser = other_ship
        else:
            winner = other_ship
            loser = self
        self.aftermath_of_battle(winner, loser)
        return self == winner

    def aftermath_of_battle(self, winner, loser):
        number_of_losses = random.randint(1, loser.state_of_crew())
        amount_of_party_rum = random.randint(1, winner.state_of_crew())
        for i in range(number_of_losses):
            loser.crew[i].die()
        for i in range(amount_of_party_rum):
            winner.crew[i].drink_some_rum()
            winner.captain.drink_some_rum()

    def __str__(self):
        return ("The pirate ship:" + "\n" +
                ("The captain of the ship has consumed {} pints of rum."
                 .format(str(self.captain.consumed_rum)) + '\n' +
                 self.captain.__str__() if isinstance(self.captain, Pirate) else "The ship doesn't have a captain.") +
                "\n" + "There are {} alive pirates in the crew.".format(self.state_of_crew()))

