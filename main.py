import random

# check whether user has responded with yes or no
def check_response(user_response):
  user_response = user_response.lower()
  if user_response == "y" or user_response == "yes":
    return True
  return False

# display whether a character is alive (Bool -> Str)
def display_life(life):
    if life:
        return "Alive"
    else:
        return "Dead"

# random health generator
# health is a number between 0-10
def random_health(upper_limit):
    return round(random.random()*upper_limit)

# check if any of the characters are alive
def any_alive(characters):
    for c in characters:
        if c.alive():
            return True
    return False

# player class - player could be Hero or Healer based on whether they have heal_points
class Player:
    def __init__(self, name, heal_points = None):
        self.name = name
        self.health = random_health(20)
        if heal_points is None:
            self.heal_points = 0
        else:
            self.heal_points = heal_points

    def get_health(self):
        return self.health

    def heal(self, player):
        if self.heal_points > 0:
            player.health += random_health(10)
            self.heal_points -= 1
        else:
            print("Your healer is tired. They cannot do anything anymore.")

    def alive(self):
        if self.health > 0:
            return True
        return False

    def attack(self):
        self.health -= random_health(3)

# monster class - health cannot be accessed directly to preserve the game element
class Monster:
    def __init__(self, name):
        self.name = name
        self.__health = random_health(10)

    def alive(self):
        if self.__health > 0:
            return True
        return False

    def attack(self):
        self.__health -= random_health(10)


print("Welcome to this exciting game of Heroes vs. Monsters! You may now create a Hero and a Healer to play.")

hero_name = input("What is the name of the Hero? ")
hero = Player(hero_name)
healer_name = input("What is the name of the Healer? ")
healer = Player(healer_name, 3)

print("Your players are born with a random number of health points.")
print("Hero health points: " + str(hero.get_health()))
print("Healer health points: " + str(healer.get_health()))

print("3 scary Monsters appear in front of you. You will now fight the Monsters in rounds.")
monsters = []
monsters.append(Monster("Cruella"))
monsters.append(Monster("EvilZap"))
monsters.append(Monster("IronMaiden"))

# check if any monsters are alive
while any_alive(monsters):
    # game only continues if hero is still alive
    if hero.alive():
        monster_number = input("Hero's turn. Which Monster do you attack? (1/2/3) ")
        monsters[int(monster_number) - 1].attack()
        user_response = input("Healer's turn. Do you want to heal? (y/n) ")
        if check_response(user_response):
            healee = input("If you want to heal yourself, input 1. If you want to heal your Hero, input 2. ")
            if int(healee) == 1:
                healer.heal(healer)
            elif int(healee) == 2:
                healer.heal(hero)
        print("Now the Monsters will play.")
        # simulating three Monster attacks on the Hero
        # future work -- Monsters can randomly attack the Healer or the Hero
        hero.attack()
        hero.attack()
        hero.attack()
        # displaying updated health points
        print("Hero health points: " + str(hero.get_health()))
        print("Healer health points: " + str(healer.get_health()))      
        print("Monster 1: " + display_life(monsters[0].alive()))
        print("Monster 2: " + display_life(monsters[1].alive()))
        print("Monster 3: " + display_life(monsters[2].alive()))
    else:
        print("Your hero is not alive anymore. Game over :(")
        break

if not any_alive(monsters):
    print("congratulations! You have won!")