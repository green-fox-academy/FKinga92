class Aircraft(object):

    def __init__(self, ammo=0):
        self.ammo = ammo
        self.max_ammo = 0
        self.base_damage = 0

    def fight(self):
        damage_dealt = self.base_damage * self.ammo
        self.ammo = 0
        return damage_dealt

    def refill(self, refill_amount):
        needed_amount = self.max_ammo - self.ammo
        if refill_amount >= needed_amount:
            self.ammo += needed_amount
            return refill_amount - needed_amount
        else:
            self.ammo +=  (refill_amount)
            return 0
    
    def get_type(self):
        return type(self).__name__

    def get_status(self):
        return ("Type {}, Ammo: {}, Base Damage: {}, All Damage: {}"
                .format(self.get_type(), self.ammo, self.base_damage, self.base_damage * self.ammo))

class F16(Aircraft):
    
    def __init__(self, ammo=0):
        super().__init__(ammo)
        self.max_ammo = 8
        self.base_damage = 30

class F35(Aircraft):
    
    def __init__(self, ammo=0):
        super().__init__(ammo)
        self.max_ammo = 12
        self.base_damage = 50

class Carrier(object):
    
    def __init__(self, stored_ammo, health_point):
        self.stored_ammo = stored_ammo
        self.health_point = health_point
        self.aircraft_store = []
    
    def add_aircraft(self, aircraft_type):
        if aircraft_type == "F16":
            self.aircraft_store.append(F16())
        elif aircraft_type == "F35":
            self.aircraft_store.append(F35())
        else:
            print("There are only two types of aircraft: F16 and F35")
        
    def needs_refill(self):
        needed_ammo = 0
        for aircraft in self.aircraft_store:
            needed_ammo += (aircraft.max_ammo - aircraft.ammo)
        return needed_ammo > 0
    
    def fill(self):
        if self.stored_ammo == 0:
            print("No ammo in storage")
        elif self.stored_ammo > 0 and self.needs_refill():
            for aircraft in self.aircraft_store:
                if aircraft.get_type() == "F35":
                    self.stored_ammo = aircraft.refill(self.stored_ammo)
            for aircraft in self.aircraft_store:
                self.stored_ammo = aircraft.refill(self.stored_ammo)
    
    def fight(self, carrier):
        if not isinstance(carrier, Carrier):
            return
        for aircraft in self.aircraft_store:
            carrier.health_point -= aircraft.fight()
    
    def get_status(self):
        if self.health_point <= 0:
            return "It's dead, Jim :("
        else:
            total_damage = 0
            status = ""
            for aircraft in self.aircraft_store:
                total_damage += (aircraft.base_damage * aircraft.ammo)
                status += aircraft.get_status() + "\n"
            status = ("HP: {}, Aircraft count: {}, Ammo Storage: {}, Total damage: {}"
                      .format(self.health_point, len(self.aircraft_store), self.stored_ammo, str(total_damage))
                      + "\n Aircrafts:\n" + status)
            return status


aircraft_carrier = Carrier(500, 5000)
aircraft_carrier.add_aircraft("F35")
aircraft_carrier.add_aircraft("F35")
aircraft_carrier.add_aircraft("F35")
aircraft_carrier.add_aircraft("F16")
aircraft_carrier.add_aircraft("F16")
aircraft_carrier.fill()
aircraft_carrier2 = Carrier(36, 2000)
aircraft_carrier2.add_aircraft("F35")
aircraft_carrier2.add_aircraft("F35")
aircraft_carrier2.add_aircraft("F16")
aircraft_carrier2.fill()
print(aircraft_carrier.get_status())
print(aircraft_carrier2.get_status())
aircraft_carrier.fight(aircraft_carrier2)
print(aircraft_carrier.get_status())
print(aircraft_carrier2.get_status())
