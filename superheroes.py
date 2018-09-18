# using randint() operator
# use // division for only integers
import random

class Ability:
    def __init__(self, name, attack_strength):
        # set ability name
        self.name = ability_name
        #
        # set attack strength
        self.attack_strength = attack_strength

    def attack(self):
        # calculate lowest and highest attack value
        # self.attack_strength = attack_strength
        # low = 0
        # high = attack_strength * 2
        #
        low = 0
        high = self.attack_strength()
        #
        # use random.randint(a,b) to select attack values
        attack = random.randint(low, high)
        #
        # return attack value between 0 and the full attack
        print(attack)

    def update_attack(self, attack_strength):
        # update attck values
        attack = self.attack()
        self.attack_strength = attack_strength

class Weapon(Ability):
    def attack(self):
        # returns random value
        
        # attack power is inherited

class Hero:
    def __init__(self, name):
        # name
        # self.name = name
        #
        # # ability list
        # self.abilities = list()

    def add_ability(self, ability):
        # add ability to ability list
        # self.append(Ability())

    def attack(self):
        # run attack() on every ability hero has
        # Call the attack method on every ability on listen
        # Return the sum of all attack values
        # print(attack_sum)

class Amor:
    def __init__(self, name, defense):
        # name
        self.name = name
        # defense
        self.defense = defense

    def defend(self):


class Team:
    def init(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        # add hero object to list of heroes

    def remove_hero(self, name):
        # remove hero from listen
        # if hero isnt found return zero

    def find_hero(self, name):
        # find and return hero from list
        # if hero isnt found return zero

    def view_all_heroes(self):
        # print out all heroes

if __name__ == "__main__":
    hero = Hero("Iron Man")
    print(hero.attack())
    ability = Ability("Repulser Blast", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Take Your Girl", 500)
    hero.add_ability(new_ability)
    print(hero.attack())
