
import random, sys

ENDING = False
Nuke = False
def start_game():
    print("Welcome to the game!")
    pokemon_intro()
    
def show_menu():
    print("Menu:")
    print("1. Start Game")
    print("0. Quit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            start_game()
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break

def pokemon_intro():
    global player_name, rival_name
    player_name = input("\n What is your name?: ")
    print("\nOak: Welcome to the world of Pokemon!")
    print("My name is Oak. People call me the Pokémon Prof.")
    print("This world is inhabited by creatures called Pokémon!")
    print("For some people, Pokémon are pets. Others use them for fights.")
    print("Myself... I study Pokémon as a profession.")
    print(f"Right, so your name is {player_name}!")
    print("This is my grandson. He's been your rival since you were a baby.")
    print(f"...Erm, what was his name now? \n")
    rival_name = input("What is your rival's name?: ")
    print(f"\nOak: That's right! I remember now! His name is {rival_name}!")
    print (f"\n{rival_name}: {player_name}!")
    print("\nOak: Your very own Pokémon legend is about to unfold! A world of dreams and adventures with Pokémon awaits! Let's go!")
    choose_starter()

import random

def choose_starter():
    starters = ["Bulbasaur", "Charmander", "Squirtle"]
    print("Welcome to the world of Pokémon!")
    print("Choose your starter Pokémon:")
    for i, pokemon in enumerate(starters, 1):
        print(f"{i}. {pokemon}")
    while True:
        try:
            choice = int(input("Enter the number of your chosen Pokémon: "))
            if 1 <= choice <= len(starters):
                break
            else:
                print("Invalid input. Please choose a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    chosen_pokemon = starters[choice - 1]
    print(f"Congratulations! You chose {chosen_pokemon} as your starter Pokémon.")
    if chosen_pokemon == starters[0]:
        rival_pokemon = starters[1]
        print(f"\n{rival_name}: I'll take this one, then!")
        print(f"\nOak: {rival_name}! That Pokémon is yours!")
        battle()
    elif chosen_pokemon == starters[1]:
        rival_pokemon = starters[2]
        print(f"\n{rival_name}: I'll take this one, then!")
        print(f"\nOak: {rival_name}! That Pokémon is yours!")
        battle()
    elif chosen_pokemon == starters[2]:
        rival_pokemon = starters[0]
        print(f"\n{rival_name}: I'll take this one, then!")
        print(f"\nOak: {rival_name}! That Pokémon is yours!")
        battle()
#The only solution to fix the IndexError: list index out of range error 
#is to ensure that the item you access from a list is within the range of the list. You can accomplish this by using the range() an len() functions


def outskirts():
  directions = ["Meadows", "Forest", "Home"]
  print("On the outskirts of Pallet Town you see a couple of sprawling routes presented to you: \nThe windy, sun-soaked meadows to the West. \nThe grass is short, and frequent travel of people through the area have left the local Pokemon quite docile to human contact and as such, aren't raring for battle. \nAlternatively, the dark, dense forest to the North offers a quick if sorivalhat risky route to your destination. Pokemon ambush travellers from the canopy above, or the underbrush. \nThe danger presented makes the area attractive for new trainers wishing to test their abilities before meeting a real challenge.")
  userInput = ""
  while userInput not in directions: # The 'not in' acts essentially as a replacement for 'break' in that if the requirements aren't fufilled then it loops back to the start.
    print("Options: Type 'meadows'/Type 'forest'/Type 'home'")
    userInput = input()
    if userInput == "meadows":
      showSafe1()
    elif userInput == "forest":
      showDangerous1()
    elif userInput == "home":
      print("Now's not the time to quit, {}!".format(player_name))
    else: 
      print("Please enter a valid option.")


def showSafe1():
  directions = ["forward", "backward"]
  print("The warm breeze brushes your face as you make your way across the meadow. \n Some herd Pokemon graze the grass off in the distance, content to ignore you. \nOff in the distance, you see the town and the clear silouhette of a Pokemon centre - the first checkpoint in your adventure. \nYour adventure is still fresh. The path through the forest is still available to you - should you turn back...")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
      Pokemoncentre1()
    elif userInput == "backward":
      outskirts()
    else:
      print("Please enter a valid option.")

def showDangerous1():
  directions = ["backward", "forward"]
  print("You walk under the dark of canopy, a sense of dread begins to weigh down on your shoulders as you hear some nearby skittering from the underbrush. \nAre you sure you wish to continue?")
  userInput = ""
  while userInput not in directions:
    print("Options: backward/forward")
    userInput = input()
    if userInput == "backward":
      outskirts()
    elif userInput == "forward":
      wildbattle1()
    else:
      print("Please enter a valid option for the adventure game.")

def wildbattle1(): #The fight code would come up here, somehow.
  actions = ["fight", "flee"]
  print("A Weedle slithers at you from out of the foliage! You can either run or fight it. What would you like to do?")
  userInput = ""
  while userInput not in actions:
    print("Options: flee/fight")
    userInput = input()
    if userInput == "fight":
        battle_wild()
        break
    elif userInput == "flee":
        showDangerous1()
    else:
        print("Please enter a valid option for the adventure game.")

def Pokemoncentre1():
  directions = ["Go to the gym", "Go home"]
  print("You are greeted chipperly by Nurse Joy upon entering the Pokemon Centre. \nAs you approach the counter, you observe around you myriad trainers and on-trainers alike are engaged in conversation. \nYou see a few unfamiliar Pokemon outside of their balls, either glued to their trainer's sides or playing with other Pokemon. \nYou approach the pink-haired nurse, where she offers to give your Pokemon a free health check - which you accept.")
  userInput = ""
  while userInput not in directions:
    print("Options: Go to the gym/Go home")
    userInput = input()
    if userInput == "Go to the gym":
      gym_one()
    elif userInput == "Go home":
      print("Deciding you've had your fill of adventure, you decide it's time to head home.")
      end1()
    else:
      print("Please enter a valid option.")

def end1():
  print("You had a short traipse to the town over. But, after some oddly mature introspection, you decided that a 10-year old has no business going so far away from home unattended.\nThe End.")

def gym_one():
  directions = ["forward", "backward"]
  print("You approach the Kusa City Gym - Home to the Kusa City Gym Leader: Lorenza 'Lass' Palestra. \nIf she had a black belt, it'd be in grass type Pokemon. She'll 'leaf' you shaking! \nIf you have any last-second preparations, now's the time to make them.")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
        gym1interior()
    elif userInput == "backward":
        print("Deciding you've had your fill of adventure, you decide it's time to head home.")
        Pokemoncentre1()
    else:
      print("Please enter a valid option.")

def gym1interior():
   print('"Boo!" says Lass')
   gym_battle()

import random
class Pokemon:
    """Blueprint for a new pokemon"""

    def __init__(self):
        self._health = 100

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        self._health = min(100, max(0, new_health))

    def attack(self, other, choice): #If you want to give attacks specific names for specific pokemon you just need to copy and paste this code and change the name of the 'class' and rename the moves.
        if choice == 1:
            attack_points = random.randint(18, 25)
        elif choice == 2:
            attack_points = random.randint(10, 35)
        else:
            print("That is not a selection. You lost your turn!")
            attack_points = 0
        other.health -= attack_points
        return attack_points

    def heal(self):
        """Heal the Pokemon"""
        heal_points = random.randint(18, 35)
        self.health += heal_points
        return heal_points
    
def battle():
    Squirtle = Pokemon()
    Charmander = user_pokemon = Pokemon()
    while True:
        print("\nATTACK CHOICES\n1. Close range attack\n2. Far range attack\n3. Heal")
        attack_choice = int(input("\nSelect an attack: "))
        # rival selects an attack, but focuses on attacking if health is full.
        rival_choice = random.randint(1, 2 if Squirtle.health == 100 else 3)
        # this is your original distinction just condensed into a single line

        # Attacks by user and rival are done simultaneously
        # with the changes to Pokemon, there is no need to save all the
        # intermediate damage/heal values -> nice and short code
        if attack_choice != 3:
            print(f"You dealt {user_pokemon.attack(Squirtle, attack_choice)} damage.")

        if rival_choice != 3:
            print(f"rival dealt {Squirtle.attack(user_pokemon, rival_choice)} damage.")

        if attack_choice == 3:
            print(f"You healed {user_pokemon.heal()} health points.")

        if rival_choice == 3:
            print(f"rival healed {Squirtle.heal()} health points.")

        if Squirtle.health == 0 or user_pokemon.health == 0:
            break

        print(f"Your current health is {user_pokemon.health}")
        print(f"rival's current health is {Squirtle.health}")

    print(f"Your final health is {user_pokemon.health}")
    print(f"rival's final health is {Squirtle.health}")

    if user_pokemon.health < Squirtle.health:
        print("\nYou lost! Better luck next time!")
    else:
        print("\nYou won against rival!")
        outskirts()

def battle_wild():
    weedle = Pokemon()
    Charmander = user_pokemon = Pokemon()
    while True:
        print("\nATTACK CHOICES\n1. Close range attack\n2. Far range attack\n3. Heal")
        attack_choice = int(input("\nSelect an attack: "))
        # rival selects an attack, but focuses on attacking if health is full.
        weedle_choice = random.randint(1, 2 if weedle.health == 100 else 3)
        # this is your original distinction just condensed into a single line

        # Attacks by user and rival are done simultaneously
        # with the changes to Pokemon, there is no need to save all the
        # intermediate damage/heal values -> nice and short code
        if attack_choice != 3:
            print(f"You dealt {user_pokemon.attack(weedle, attack_choice)} damage.")

        if weedle_choice != 3:
            print(f"rival dealt {weedle.attack(user_pokemon, weedle_choice)} damage.")

        if attack_choice == 3:
            print(f"You healed {user_pokemon.heal()} health points.")

        if weedle_choice == 3:
            print(f"weedle healed {weedle.heal()} health points.")

        if weedle.health == 0 or user_pokemon.health == 0:
            break

        print(f"Your current health is {user_pokemon.health}")
        print(f"rival's current health is {weedle.health}")

    print(f"Your final health is {user_pokemon.health}")
    print(f"rival's final health is {weedle.health}")

    if user_pokemon.health < weedle.health:
        print("\nYou lost! Better luck next time!")
    else:
        print("\nYou won against the weedle! You found its treasure: A small-scale WMD.")
        Pokemoncentre1()
        nuke = True

def gym_battle():
    Oddish = Pokemon()
    Charmander = user_pokemon = Pokemon()
    while True:
        print("\nATTACK CHOICES\n1. Close range attack\n2. Far range attack\n3. Heal")
        attack_choice = int(input("\nSelect an attack: "))
        # rival selects an attack, but focuses on attacking if health is full.
        Oddish_choice = random.randint(1, 2 if Oddish.health == 200 else 3)
        # this is your original distinction just condensed into a single line

        # Attacks by user and rival are done simultaneously
        # with the changes to Pokemon, there is no need to save all the
        # intermediate damage/heal values -> nice and short code
        if attack_choice != 3:
            print(f"You dealt {user_pokemon.attack(Oddish, attack_choice)} damage.")

        if Oddish_choice != 3:
            print(f"rival dealt {Oddish.attack(user_pokemon, Oddish_choice)} damage.")
        if attack_choice == 3:
            print(f"You healed {user_pokemon.heal()} health points.")

        if Oddish_choice == 3:
            print(f"weedle healed {Oddish.heal()} health points.")

        if Oddish.health == 0 or user_pokemon.health == 0:
            break

        print(f"Your current health is {user_pokemon.health}")
        print(f"rival's current health is {Oddish.health}")

    print(f"Your final health is {user_pokemon.health}")
    print(f"rival's final health is {Oddish.health}")

    if user_pokemon.health < Oddish.health:
        print("\nYou lost! Better luck next time!")
    else:
        print("\nYou kicked her ass!")
        print("\nGood job!")
        end2()

def end2():
    print("Congratulations in beating the first gym.\nThe upcoming journey will be long, difficult, but rewarding.\n\nYou've proven you have what it takes to become a Pokemon master.")
    print("Thank you for playing.")
    print(":)") 
    ENDING = True
    if ENDING == True:
       sys.exit()
def end3():
    print("In your surprise, you nuke the gym leader, destroying the town and surrounding area. RIP Bozo.")
    ENDING = True
    if ENDING == True:
       sys.exit()

if __name__ == "__main__" and ENDING == False:
    main()