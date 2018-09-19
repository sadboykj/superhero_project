# using randint() operator
# use // division for only integers
import random

class Hero:
    def __init__(self, name):
        # name
        self.name = name
        #
        # ability list
        self.abilities = list()

    def add_ability(self, ability):
        # add ability to ability list
        self.abilities.append(ability)

    def attack(self):
        # initialize attack sum and power sum
        power = 0
        # power_sum = 0
        # count how many abilities hero has
        for ability in self.abilities:
            power += ability.attack()
            # power_sum += number_of.attack_strength()
        # return the number of abilities
        return (power)
        # return (power_sum)
        # prints number of abilities
        # print(len(self.abilities))

class Ability:
    def __init__(self, name, attack_strength):
        # set ability name
        self.name = name
        #
        # set attack strength
        self.attack_strength = attack_strength

    def attack(self):
        # calculate lowest and highest attack value
        # self.attack_strength = attack_strength
        # low = 0
        # high = attack_strength * 2
        #
        low = self.attack_strength // 2
        high = self.attack_strength
        #
        # use random.randint(a,b) to select attack values
        attack_power = random.randint(low, high)
        #
        # return attack value between 0 and the full attack
        return (attack_power)

    def update_attack(self, attack_strength):
        # update attck values
        self.attack_strength = attack_strength

# class Weapon(Ability):
#     def attack(self):
#         # returns random value
#         # attack power is inherited
#         low = 0
#         high = self.attack_strength()
#         attack = random.randint(low, high)
#         #
#         print(attack)
#
# class Amor:
#     def __init__(self, name, defense):
#         # name
#         self.name = name
#         # defense
#         self.defense = defense
#
#     def defend(self):
#
#
# class Team:
#     def init(self, team_name):
#         self.name = team_name
#         self.heroes = list()
#
#     def add_hero(self, Hero):
#         # add hero object to list of heroes
#
#
#     def remove_hero(self, name):
#         # remove hero from listen
#         # if hero isnt found return zero
#
#     def find_hero(self, name):
#         # find and return hero from list
#         # if hero isnt found return zero
#
#     def view_all_heroes(self):
#         # print out all heroes

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
