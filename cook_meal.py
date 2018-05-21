
#define classes

#define recipe class
class Recipe:

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients_needed = ingredients

    def __lt__(self, ingredient):
        self.ingredients.append(ingredient)

    def list_ingredients(self):
        print(self.ingredients_needed)


#define ingredient class
class Ingredient:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "self.name"

#define chef class
class Chef:

    def __init__(self, name):
        self.name = name

    def goes_shopping(self, recipe, ingredient):
        recipe < ingredient





#start program
ramen_noodles = Recipe("Ramen Noodles", ["noodles", "water", "egg"])

ramen_noodles.list_ingredients()
