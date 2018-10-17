import random

class Ability:
    def __init__(self, name, attack_strength):
        self.attack_strength = attack_strength
        self.name = name

    def attack(self):
        """
        return attack value
        """
        return random.randint(self.attack_strength // 2, self.attack_strength)

    def update_attack(self, attack_strength):
        """
        update attack value
        """
        self.attack_strength = attack_strength

class Hero:
    #
    name = ''
    abilities = list()
    weapons = list()
    armors = list()
    start_health = 0
    health = 0
    deaths = 0
    kills = 0

    def __init__(self, name):
        """
        Initialize starting values
        """
        self.abilities = list()
        self.name = name
        #
        self.weapons = list()
        self.armors = list()
        self.start_health = int(health)
        self.health = int(health)
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        """
        Add ability to abilities list
        """
        self.abilities.append(ability)

    def add_armor(self, armor):
        """
        Add armor to armor list
        """
        self.armor.append(armor)

    def add_weapon(self, weapon):
        """
        Add weapon to weapon list
        """
        self.weapon.append(weapon)

    def attack(self):
        """
        Run attack() on every ability hero has
        """
        attack_pwr = 0
        #
        if self.health <= 0:
            return 0
        #
        for ability in self.abilities:
            attack_pwr += ability.attack()
        #
        for weapon in self.weapons:
            attack_pwr += weapon.attack()
        #
        return attack_pwr

    def defend(self):
        """
        Calculate defense power
        """
        defense_pwr = 0
        #
        if self.health <= 0:
            return 0
        #
        for armor in self.armors:
            defense_pwr += amor.defend()
        #
        return defense_pwr

    def take_damage(self, damage):
        """
        Calculate defense power
        """
        if self.health > 0:
            self.health -= damage
            #
            if self.health <= 0:
            self.deaths += 1
            return 1
        #
        return 0


class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        """
        attack_power = randint(0, self.attack_strength)
        return attack_power

class Team:
    def init(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """
        Add Hero object to heroes list.
        """
        self.heroes.append(Hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        self.heroes.remove(Hero)

    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        if (self.heroes.find(Hero)):
            return Hero
        else:
            return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        print(self.heroes)

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """
        self.team_one = Team('Avengers')

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
        self.team_two = Team('Evil League of EVIL')

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """

    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
