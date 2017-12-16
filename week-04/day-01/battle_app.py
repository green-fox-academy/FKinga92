from pirate import Pirate
from pirate_ship import Ship

black_pearl = Ship()
black_pearl.fill_ship()
print(black_pearl)
flying_dutchman = Ship()
flying_dutchman.fill_ship()
print(flying_dutchman)
black_pearl.battle(flying_dutchman)
print(black_pearl)
print(flying_dutchman)