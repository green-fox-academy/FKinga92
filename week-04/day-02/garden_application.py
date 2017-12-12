class Garden(object):

    def __init__(self):
        self.flowers = []
        self.trees = []
    
    def add_flower(self, Flower):
        self.flowers.append(Flower)
    
    def add_tree(self, Tree):
        self.trees.append(Tree)
    
    def water(self, amount_of_water):
        need_water = 0
        for flower in self.flowers:
            need_water = need_water + 1 if flower.needs_water else need_water
        for tree in self.trees:
            need_water = need_water + 1 if tree.needs_water else need_water
        for flower in self.flowers:
            if flower.needs_water:
                flower.get_watered(amount_of_water / need_water)  
        for tree in self.trees:
            if tree.needs_water:
                tree.get_watered(amount_of_water / need_water)
    def get_status(self):
        for flower in self.flowers:
            water_needed = "needs water" if flower.needs_water else "doesn't need water"
            print("The " + flower.color + " Flower " + water_needed)
        for tree in self.trees:
            water_needed = "needs water" if tree.needs_water else "doesn't need water"
            print("The " + tree.color + " Tree " + water_needed)


class Flower(object):

    def __init__(self, water_amount, color):
        self.water_amount = int(water_amount)
        self.color = color
        self.needs_water = True

    def get_watered(self, amount_of_water):
        self.water_amount += amount_of_water * 0.75
        self.needs_water = True if self.water_amount < 5 else False

class Tree(Flower):

    def __init__(self, water_amount, color):
        super().__init__(water_amount, color)
        self.needs_water = True
    
    def get_watered(self, amount_of_water):
        self.water_amount += amount_of_water * 0.4
        self.needs_water = True if self.water_amount < 10 else False

my_garden = Garden()
yellow_flower = Flower(0, "yellow")
blue_flower = Flower(0, "blue")
purple_tree = Tree(0, "purple")
orange_tree = Tree(0, "orange")
my_garden.add_flower(yellow_flower)
my_garden.add_flower(blue_flower)
my_garden.add_tree(purple_tree)
my_garden.add_tree(orange_tree)
my_garden.get_status()
my_garden.water(40)
print("\n" + "Watering with 40")
my_garden.get_status()
my_garden.water(70)
print("\n" + "Watering with 70")
my_garden.get_status()
