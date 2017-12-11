from fleet import Fleet
from thing import Thing

fleet = Fleet()
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch


milk = Thing("Get milk")
obstacle = Thing("Remove the obstacles")
stand_up = Thing("Stand up")
stand_up.complete()
lunch = Thing("Eat lunch")
lunch.complete()

fleet.add(milk)
fleet.add(obstacle)
fleet.add(stand_up)
fleet.add(lunch)


print(fleet)
