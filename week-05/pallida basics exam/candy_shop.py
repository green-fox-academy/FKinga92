# We run a Candy shop where we sell candies and lollipops
    # One lollipop's price is 10$
        # And it made from 5gr of sugar
    # One candie's price is 20$
        # And it made from 10gr of sugar
# we can raise their prices with a given percentage
#
# Create a CandyShop class
# It can store sugar and money as income. The constructor should take the amount of sugar in gramms.
# we can create lollipops and candies store them in the CandyShop's storage
# If we create a candie or lollipop the CandyShop's sugar amount gets reduced by the amount needed to create the sweets
# We can raise the prices of all candies and lollipops with a given percentage
# We can sell candie or lollipop with a given number as amount
# If we sell sweets the income will be increased by the price of the sweets and we delete it from the inventory
# We can buy sugar with a given number as amount. The price of 1000gr sugar is 100$
# If we buy sugar we can raise the CandyShop's amount of sugar and reduce the income by the price of it.
# The CandyShop should be represented as string in this format:
# "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"

class Sweets(object):

    def __init__(self):
        self.price = 0
        self.needed_sugar_amount = 0

    def raise_price(self, price_raise_rate):
        self.price *= (1 + price_raise_rate / 100)

class Candy(Sweets):

    def __init__(self):
        self.price = 20
        self.needed_sugar_amount = 10

class Lollipop(Sweets):

    def __init__(self):
        self.price = 10
        self.needed_sugar_amount = 5

class CandyShop(object):

    def __init__(self, sugar_storage):
        self.sugar_storage = sugar_storage
        self.income = 0
        self.candies = []
        self.lollipops = []

    def create_sweets(self, candy):
        if candy.lower() == "candy":
            self.candies.append(Candy())
            self.sugar_storage -= 10
        elif candy.lower() == "lollipop":
            self.lollipops.append(Lollipop())
            self.sugar_storage -= 5
        else:
            print("Unfortunately, we do not have the recipe for that.")

    def raise_prices(self, raise_rate):
        for candy in self.candies:
            candy.raise_price(raise_rate)
        for lollipop in self.lollipops:
            lollipop.raise_price(raise_rate)

    def sell(self, candy, amount):
        if candy.lower() == "candy":
            for i in range(amount):
                for sweet in self.candies:
                    self.income += sweet.price
                    self.candies.remove(sweet)
        elif candy.lower() == "lollipop":
            for i in range(amount):
                for lollipop in self.lollipops:
                    self.income += lollipop.price
                    self.lollipops.remove(lollipop)

    def buy_sugar(self, amount):
        self.sugar_storage += amount
        self.income -= (amount * 0.1)

    def __str__(self):
        return ("Inventory: {} candies, {} lollipops, Income: {}, Sugar: {}gr"
                .format(len(self.candies), len(self.lollipops), self.income, self.sugar_storage))



candy_shop = CandyShop(300)
candy_shop.create_sweets("candy")
candy_shop.create_sweets("candy")
candy_shop.create_sweets("lollipop")
candy_shop.create_sweets("lollipop")
print(candy_shop)
# Should print out:
# Invetory: 2 candies, 2 lollipops, Income: 0, Sugar: 270gr
candy_shop.sell("candy", 1)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 2 lollipops, Income:20, Sugar: 270gr"
candy_shop.raise_prices(5)
candy_shop.sell("lollipop", 1)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:30.5, Sugar: 270gr"
candy_shop.buy_sugar(300)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:0.5, Sugar: 570gr"
