
#define classes

#define recipe class
class Recipe:

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients_needed = ingredients
        self.count = 0

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
            return False
        else:
            return True

#define eater class
class Eater():

    def __init__(self, name, allergy):
        self.name = name
        self.allergy = allergy

    def __repr__(self):
        return self.name

    def eat_meal(self, recipe):

        if not recipe.safe_to_eat(self):
            print(f"It is not safe for {self.name} to eat {recipe}!")
        elif recipe.count <= 0:
            print(f"Sorry, but there isn't any {recipe} prepared for {self.name} to eat.")
        else:
            print(f"{self.name} noms on some {recipe}.")
            recipe.count -= 1


#define chef class
class Chef(Eater):

    def __init__(self, name, allergy):
        self.has_ingredients = []
        super().__init__(name, allergy)

    def __repr__(self):
        return self.name

    def __lt__(self, ingredient):
        self.has_ingredients.append(ingredient)

    def goes_shopping(self, recipe):
        print(f"{self.name} goes shopping for the ingredients to make {recipe.name}.")

        for item in recipe.ingredients_needed:
            self.has_ingredients.append(item)

    def prepare_meal(self, recipe):
        if recipe.has_ingredients(self):
            print(f"{self.name} prepares {recipe} and it's ready to eat!")
            self.has_ingredients = []
            recipe.count += 1
        else:
            print(f"{self.name} is missing something to make {recipe}.")






#start program
ramen_noodles = Recipe("Ramen Noodles", ["noodles", "water", "eggs"])
pb_and_j = Recipe("PB and J", ["bread", "peanut butter", "jelly"])
chef_john = Chef("John", None)
chris = Eater("Chris", "peanut butter")
robert = Eater("Robert", None)



chris.eat_meal(pb_and_j)
chef_john.prepare_meal(pb_and_j)
chef_john.goes_shopping(ramen_noodles)
chef_john.prepare_meal(ramen_noodles)
chris.eat_meal(ramen_noodles)

robert.eat_meal(pb_and_j)
chef_john.goes_shopping(pb_and_j)
chef_john.prepare_meal(pb_and_j)
chef_john.goes_shopping(pb_and_j)
chef_john.prepare_meal(pb_and_j)
robert.eat_meal(pb_and_j)
chef_john.eat_meal(pb_and_j)
