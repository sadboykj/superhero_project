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
        # amor list
        self.amors = list()
        #
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    # str returns string representation
    # works like .format
    def __str__(self):
        return self.name

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

    def defend(self):
        defense = 0

        if len(self.amors) == 0:
            return 0

        for power_of in self.armors:
            # defense = defense + powerOf.defense
            defense += power_of.defend()

        if self.health == 0:
            defense = 0
            return defense
        else:
            return defense

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
        power = random.randint(low, high)
        #
        # return attack value between 0 and the full attack
        return (power)

    def update_attack(self, attack_strength):
        # update attck values
        self.attack_strength = attack_strength

class Weapon(Ability):
    def attack(self):
        # returns random value
        # attack power is inherited
        power = random.randint(0, self.attack_strength)
        print(power)

class Team:
    def init(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        # add hero object to list of heroes
        self.heroes.append(Hero)


    def remove_hero(self, name):
        # remove hero from listen
        # if hero isnt found return zero
        # to remove all heroes:
        # self.heroes.clear()
        # or del self.heroes[:]
        # .remove removes the first matching value
        # del[] and .pop remove the index
        # but .pop also returns it
        



    def find_hero(self, name):
        # find and return hero from list
        # if hero isnt found return zero

    def view_all_heroes(self):
        # print out all heroes
        print self.heroes


# class Amor:
#     def __init__(self, name, defense):
#         # name
#         self.name = name
#         # defense
#         self.defense = defense
#
#     def defend(self):
#

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
