
#define classes

#define recipe class
class Recipe:

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients_needed = ingredients

    def __repr__(self):
        return self.name

    def __lt__(self, ingredient):
        self.ingredients.append(ingredient)

    def list_ingredients(self):
        print(self.ingredients_needed)

    def has_ingredients(self, chef):
        if self.ingredients_needed == chef.has_ingredients:
            return True
        else:
            return False

    def safe_to_eat(self, eater):
        if eater.allergy in self.ingredients_needed:
            print(f"{self.name} is not safe for {eater} to eat!")
        else:
            print(f"{eater} can chow down on some {self.name}!")

    def prepare_meal(self, chef):

        if self.has_ingredients(chef):
            print(f"{chef} prepares {self.name} and it's ready to eat!")
            chef.has_ingredients = []
        else:
            print(f"{chef} is missing something to make {self.name}.")




#define chef class
class Chef:

    def __init__(self, name):
        self.name = name
        self.has_ingredients = []

    def __repr__(self):
        return self.name

    def __lt__(self, ingredient):
        #print(f"{self.name} goes shopping for {ingredient}.")
        self.has_ingredients.append(ingredient)

    def goes_shopping(self, recipe):
        print(f"{self.name} goes shopping for the ingredients to make {recipe.name}.")

        for item in recipe.ingredients_needed:
            self.has_ingredients.append(item)


#define eater class
class Eater:

    def __init__(self, name, allergy):
        self.name = name
        self.allergy = allergy

    def __repr__(self):
        return self.name


#start program
ramen_noodles = Recipe("Ramen Noodles", ["noodles", "water", "eggs"])
pb_and_j = Recipe("PB and J", ["bread", "peanut butter", "jelly"])
chef_john = Chef("John")
chris = Eater("Chris", "peanut butter")
robert = Eater("Robert", "none")


ramen_noodles.prepare_meal(chef_john)
chef_john.goes_shopping(ramen_noodles)
ramen_noodles.prepare_meal(chef_john)
