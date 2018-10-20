import random
# got os from Luc
import os

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
    #
    def __init__(self, name, health=100):
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
        self.armors.append(armor)

    def add_weapon(self, weapon):
        """
        Add weapon to weapon list
        """
        self.weapons.append(weapon)

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
        Calculates then returns defense power
        """
        defense_pwr = 0
        #
        if self.health <= 0:
            return 0
        #
        for a in self.armors:
            defense_pwr += a.defense()
        #
        return defense_pwr

    def take_damage(self, damage):
        """
        Calculates defense power
        Returns 1 for death
        """
        if self.health > 0:
            self.health -= damage
        #
            if self.health <= 0:
                self.deaths += 1
            return -1
        #
        return 0

    def add_kill(self, num_kills):
        self.kills += num_kills


class Ability:
    # variables protect function when parameters aren't passed
    # is there a better way to protecc?
    name = ''
    attack_strength = 0
    #
    def __init__(self, name, attack_strength):
        """
        attack strength =
        random int between attack strength and half attack strength
        random.randint(self.attack_strength // 2, self.attack_strength)
        """
        self.name = name
        min_pwr = int(attack_strength) // 2
        self.attack_strength = random.randint(min_pwr, int(attack_strength))

    def attack(self):
        """
        return attack strength
        """
        return self.attack_strength

    def update_attack(self, attack_strength):
        """
        update attack value
        """
        self.attack_strength = attack_strength


class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        """
        attack_pwr = randint(0, self.attack_strength)
        return attack_pwr


class Armor:
    name = ''
    defense = 0
    #
    def __init__(self, name, defense):
        self.name = name
        self.defense = int(defense)

    def defense(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        """
        defense_pwr = randint(0, self.defense)
        return defense_pwr


class Team:
    name = ''
    heroes = list()
    #
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """
        Add Hero object to heroes list.
        """
        self.heroes.append(Hero)

    def remove_hero(self, name):
        """
        Run through hero list to check if hero exists.
        Remove hero from heroes list.
        If hero isn't found return 0.
        """
        # guesss: self.heroes.remove(Hero)
        index = 0
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.pop(index)
                # return none in order to stop function
                return None
            index += 1
        #
        return 0


    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        # guess:
        # if (self.heroes.find(Hero)):
        #     return Hero
        # else:
        #     return 0
        for hero in self.heroes:
            if hero.name == name:
                return hero

    def view_all_heroes(self):
        """
        Print out all heroes to the console.
        """
        for hero in self.heroes:
            print(hero.name)

    def attack(self, target):
        """
        Sum total of each hero's attack power
        Counts kills
        """
        attack_pwr = 0
        for hero in self.heroes:
            attack_pwr += hero.attack()
        #
        killCheck = target.defend(attack_pwr)
        self.update_kills(killCheck)

    def defend(self, dmg):
        """
        Disperses damage
        """
        # damage = dmg
        defense_pwr = 0
        kills = 0
        for hero in self.heroes:
            defense_pwr += hero.defend()
        #
        damage = dmg - defense_pwr
        self.deal_damage(damage)
        #
        dmg_piece = damage // len(self.heroes)
        if damage > 0:
            for hero in self.heroes:
                dead = hero.take_damage(dmg_piece)
                if dead == -1:
                    kills += 1
        #
        return kills

    def deal_damage(self, dmg):
        """
        Disperses damage to target team
        """
        deaths = 0
        if dmg > 0:
            dmg_piece = dmg // len(self.heroes)
            for hero in self.heroes:
                dead = hero.take_damage(dmg_piece)
                if dead == -1:
                    deaths += 1
        #
        return deaths

    def stats(self):
        """
        Lists out hero kills
        """
        for hero in self.heroes:
            print("{}:\nKills: {}\nDeaths: {}".format(
            hero.name, hero.kills, hero.deaths))

    def revive_heroes(self, health=100):
        """
        Resets heroes health
        """
        for hero in self.heroes:
            hero.health = hero.start_health

    def check_heroes(self):
        for hero in self.heroes:
            if hero.health > 0:
                return True
        #
        return False

    def update_kills(self, kills):
        for hero in self.heroes:
            hero.add_kill(kills)

class Arena:
    team_one = None
    team_two = None
    #
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team(self, team):
        team_name = user_input('Enter name for team {}: '.format(team))
        team = Team(team_name)
        add_heroes = True
        hero_count = 1

        while add_heroes:
            name = user_input('Enter name for hero {}: '.format(hero_count))
            health = user_input('Enter health for {}: default(100) '.format(name))

            hero = Hero(name, health)

            add_ab = user_input('Add abilities to {}? (y/n) '.format(name))
            if add_ab.lower() == 'y':
                have_abilities = True
            elif add_ab.lower() == 'n':
                have_abilities = False
            while have_abilities:
                ab_name = user_input('Enter name for ability: ')
                ab_power = user_input('Enter power for {}: '.format(ab_name))
                ability = Ability(ab_name, ab_power)
                hero.add_ability(ability)
                add_another = user_input('Add another ability to {}? (y/n) '.format(name))
                if add_another.lower() == 'n':
                    have_abilities = False

            add_wp = user_input('Add weapons to {}? (y/n) '.format(name))
            if add_wp.lower() == 'y':
                have_weapons = True
            elif add_wp.lower() == 'n':
                have_weapons = False
            while have_weapons:
                wp_name = user_input('Enter name for weapon: ')
                wp_power = user_input('Enter power for {}: '.format(wp_name))
                weapon = Weapon(wp_name, wp_power)
                hero.add_weapon(weapon)
                add_another = user_input('Add another weapon to {}? (y/n) '.format(name))
                if add_another.lower() == 'n':
                    have_weapons = False

            add_ar = user_input('Add armor to {}? (y/n) '.format(name))
            if add_ar.lower() == 'y':
                have_armor = True
            elif add_ar.lower() == 'n':
                have_armor = False
            while have_armor:
                ar_name = user_input('Enter name for armor: ')
                ar_power = user_input('Enter power defense for {}: '.format(ar_name))
                armor = Armor(ar_name, ar_power)
                hero.add_armor(armor)
                add_another = user_input('Add more armor to {}? (y/n) '.format(name))
                if add_another.lower() == 'n':
                    have_armor = False


            team.add_hero(hero)
            hero_count += 1
            print('Created {} as a hero for team {}.'.format(name, team_name))
            add_another = user_input('Add another hero to team {}? (y/n) '.format(team_name))
            if add_another.lower() == 'n':
                    add_heroes = False

        return team

    # def build_team_one(self):
    #
    # def build_team_two(self):

    def team_battle(self):
        teams_alive = True
        while teams_alive:
            team_one_alive = self.team_one.check_heroes()
            team_two_alive = self.team_two.check_heroes()

            if team_one_alive and team_two_alive:
                self.team_one.attack(self.team_two)
                self.team_two.attack(self.team_one)
            else:
                teams_alive = False

        self.show_stats()
        print('\n\n')
        reset = user_input('Run simulation again? (y/n): ')
        if reset.lower() == 'y':
            self.reset()

    def show_stats(self):
        print('{} statistics:\n\n'.format(self.team_one.name))
        self.team_one.stats()

        print('__________________________________________________')

        print('{} statistics:\n\n'.format(self.team_two.name))
        self.team_two.stats()


def user_input(prompt):
    try:
        user_input = input(prompt)
        os.system('cls' if os.name == 'nt' else 'clear')
        return user_input

    except EOFError:
        return ''


if __name__ == "__main__":
    arena = Arena()
    arena.team_one = arena.build_team(1)
    arena.team_two = arena.build_team(2)
    arena.team_battle()
