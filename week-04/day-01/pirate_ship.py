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
        i = 0
        while i <= random.randint(1, 100):
            crew_member = Pirate()
            self.crew.append(crew_member)
            i += 1

    def state_of_crew(self):
        number_of_alive_pirates = 0
        for pirate in self.crew:
            if pirate.alive:
                number_of_alive_pirates += 1
        return number_of_alive_pirates

    def get_ship_score(self):
        return self.state_of_crew() - self.captain.consumed_rum

    battle_winner = None
    battle_loser = None

    def battle(self, other_ship):
        Ship.battle_winner = (self if isinstance(other_ship, Ship) and
                  self.get_ship_score() > other_ship.get_ship_score() else other_ship)
        Ship.battle_loser = (self if isinstance(other_ship, Ship) and
                 self.get_ship_score() < other_ship.get_ship_score() else other_ship)
        self.aftermath_of_battle(other_ship)
        return True if Ship.battle_winner == self else False

    def aftermath_of_battle(self, other_ship):
        number_of_losses = random.randint(1, len(Ship.battle_loser.crew) - 1)
        amount_of_party_rum = random.randint(1, len(Ship.battle_winner.crew) - 1)
        for i in range(number_of_losses):
            Ship.battle_loser.crew[i].die()
        for i in range(amount_of_party_rum):
            Ship.battle_winner.crew[i].drink_some_rum()
            Ship.battle_winner.captain.drink_some_rum()

    def __str__(self):
        return ("The pirate ship:" + "\n" +
                ("The captain of the ship has consumed {} pints of rum."
                 .format(str(self.captain.consumed_rum)) + '\n' +
                 self.captain.__str__() if isinstance(self.captain, Pirate) else "The ship doesn't have a captain.") +
                "\n" + "There are {} alive pirates in the crew.".format(self.state_of_crew()))

black_pearl = Ship()
black_pearl.fill_ship()
print(black_pearl)
flying_dutchman = Ship()
flying_dutchman.fill_ship()
print(flying_dutchman)
black_pearl.battle(flying_dutchman)
print(black_pearl)
print(flying_dutchman)
