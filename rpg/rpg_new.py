#IMPORTS
import random
from settings import *

#varibles
pulse_cartridge = 20
global small_kit
global medium_kit
global large_kit
global mini_hospital
global in_combat
in_combat = False
small_kit = 1
medium_kit = 0
large_kit = 0
mini_hospital = 0
global invatory
invatory = ["pulse pistol","tesla stick","tesla rifle","small kit","medium kit","large kit","mini hospital"]
global health
health = settings.MAX_HEALTH
global current_weapon
current_weapon = 0

#game code

def encounter_enemy():
    enemy_list = ["AssdDrone", "ALD", "assdDrone"]
    enemy_name = random.choice(enemy_list)
    enemy_settings = getattr(settings, enemy_name.lower(), None)
    if enemy_settings is None:
        raise ValueError(f"Enemy settings not found for {enemy_name}")
    return enemy_name, enemy_settings


def attack(enemy_name, enemy_settings, weapon_settings, extra):
    damage = weapon_settings["damage"] + extra
    enemy_health = enemy_settings["health"]
    enemy_health -= damage
    return damage, enemy_health


def change_weapon(inventory):
    global current_weapon
    print("Current weapons in inventory:")
    for index, weapon in enumerate(inventory):
        print(f"{index + 1}. {weapon}")

    # Get user input for the selected weapon
    while True:
        try:
            choice = int(input("Enter the number of the weapon to switch to (0 to cancel): "))
            if 0 <= choice <= len(inventory):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Switch to the selected weapon
    if choice != 0:
        selected_weapon = inventory.pop(choice - 1)
        inventory.insert(0, selected_weapon)
        current_weapon = choice - 1  # Update the current_weapon variable
        print(f"You switched to {selected_weapon}.")
    else:
        print("Weapon change canceled.")

def check_inv():
    global small_kit
    global medium_kit
    global large_kit
    global mini_hospital
    global health  
    print("pulse cartridge:", pulse_cartridge)
    
    for item in invatory:
        if item == "tesla stick":
            print(settings.teslastick)
        elif item == "tesla rifle":
            print(settings.teslarifle)
        elif item == "pulse pistol":
            print(settings.pulsepistol)
        elif item == "small kit":
            print(settings.smallkit)
            print("quantity", small_kit)
        elif item == "medium kit":
            print(settings.mediumkit)
            print("quantity", medium_kit)
        elif item == "large kit":
            print(settings.largekit)
            print("quantity", large_kit)
        elif item == "mini hospital":
            print(settings.minihospital)
            print("quantity", mini_hospital)

    if small_kit > 0 or medium_kit > 0 or large_kit > 0 or mini_hospital > 0:
        while True:
            if health > 200:
                health = 200
            action = input(f"Your health is {health}. Would you like to use a kit? (y/n): ")
            if action == "y":
                action = input("""Press 1 for small kit
                                  Press 2 for medium kit
                                  Press 3 for large kit
                                  Press 4 for mini hospital
                                  Press 0 to cancel
                                  :>""")
                if action == "1" and small_kit > 0:
                    health += settings.smallkit["health"]
                    small_kit -= 1
                    if health > 200:
                        health = 200
                    print("Consumed small kit. Health is now", health) 
                elif action == "2" and medium_kit > 0:
                    health += settings.mediumkit["health"]
                    medium_kit -= 1
                    if health > 200:
                        health = 200
                    print("Consumed medium kit. Health is now", health) 
                elif action == "3" and large_kit > 0:
                    health += settings.largekit["health"]
                    large_kit -= 1 
                    if health > 200:
                        health = 200
                    print("Consumed large kit. Health is now", health)
                elif action == "4" and mini_hospital > 0:
                    health += settings.minihospital["health"]
                    mini_hospital -= 1
                    if health > 200:
                        health = 200
                    print("Consumed mini hospital. Health is now", health) 
                elif action == "0":
                    print("Canceling")
                    break
                else:
                    print("Invalid choice or insufficient quantity. Choose another option.")
            elif action == "n":
                break


def combat_loop(enemy_name, enemy_settings, weapons_inventory):
    global health
    global small_kit
    global medium_kit
    global large_kit
    global mini_hospital
    global current_weapon

    print(f"You encountered a {enemy_name}!")
    enemy_health = enemy_settings["health"]
    while health > 0 and enemy_health > 0:
        action = input("Press 'a' to attack, 'e' to escape, or 'c' to change weapon: > ")

        if action == 'a':
            # Attack with the current weapon
            current_weapon_name = weapons_inventory[current_weapon]
            current_weapon_settings = getattr(settings, current_weapon_name.replace(" ", "").lower(), None)

            if current_weapon_settings is None:
                raise ValueError(f"Weapon settings not found for {current_weapon_name}")

            extra = random.randint(3, 10)
            damage = current_weapon_settings["damage"] + extra
            enemy_health -= damage
            print(f"You dealt {damage} damage plus {extra} extra. Enemy health is now {enemy_health}.")

            if enemy_health <= 0:
                print("You defeated the enemy!")
                # ... (rest of the code remains unchanged)
            else:
                # Enemy's turn
                enemy_damage = random.randint(enemy_settings["damage-low"], enemy_settings["damage-high"])
                health -= enemy_damage
                print(f"The enemy dealt {enemy_damage} damage. Your health is now {health}.")

                if health <= 0:
                    print("You died.")
                    break

        elif action == 'e':
            print("You escaped from the enemy.")
            break

        elif action == 'c':
            change_weapon(invatory)

        else:
            print("Invalid input. Press 'a' to attack, 'e' to escape, or 'c' to change weapon.")

        global in_combat
        in_combat = False  # Reset in_combat flag after the combat loop






def game():
    global small_kit
    global medium_kit
    global large_kit
    global mini_hospital
    global health
    global in_combat
    # variables
    health = settings.MAX_HEALTH
    name = input("you're having trouble remembering your name, what is it: > ")

    # game
    print('new weapon "tesla stick"')

    while health > 0:  # Check if the player is still alive
        action = input("Press 'w' to walk or 'e' to check inventory: > ")

        if action == 'w':
            if random.randint(1, 4) == 1:
                enemy_name, enemy_settings = encounter_enemy()
                in_combat = True
                combat_loop(enemy_name, enemy_settings, invatory[1:])  # Pass weapons_inventory
                in_combat = False  # Combat ended, reset the flag
            else:
                print("You walked to the next room.")

        elif action == 'e':
            check_inv()

        else:
            print("Invalid input. Press 'w' to walk or 'e' to check inventory.")

    print("Game over. You died.")






def turtoial():
    global small_kit
    global medium_kit
    global large_kit
    global mini_hospital
    global health 
    global invatory
    health -= 20
    print("welcome to the turtoial")
    print("in this game you will walk between rooms while running into enemys and managing your weapons and invetory")
    print("starting scenario")
    while True:
        input("every turn of the game you will see a prompt like the following <press w to walk or press e to check invatory> presss w:>")
        print("you walked to the next room")
        input("every turn of the game you will see a prompt like the following <press w to walk or press e to check invatory> presss e:>")
        print("what you see is the invatory screen it will show what health kits you have as well as what weapons you have and there states/ammo")
        print("you may notice the tesla stick and rifle read ammo none this means that dont cossume ammo")
        print("you may also notice the tesla stick and pulse pistol have a type this reffers to a damage multiplyer if you use the correct weapon on a enemy for example the pulse pistol is a soft weapon meaning it will do extra damage agasint soft enemys")
        print("pulse cartdige:",pulse_cartridge)
        if "tesla stick"in invatory:
            print(settings.teslastick)
        if "tesla rifle"in invatory:
            print(settings.teslarifle)
        if "pulse pistol"in invatory:
            print(settings.pulsepistol)
        if "small kit" in invatory:
            print(settings.smallkit)
            print("quanity",small_kit)
        if "medium kit" in invatory:
            print(settings.mediumkit)
            print("quanity",medium_kit)
        if "large kit" in invatory:
            print(settings.largekit)
            print("quanity",large_kit)
        if "mini hospital" in invatory:
            print(settings.minihospital)
            print("quanity",mini_hospital)
        print("the following prompt is the health kit selection each time you check you invatory you can use a health kit your current health is 180 max health is 200 press y")
        if small_kit or medium_kit or large_kit or mini_hospital > 1:
            while True:
                action = input(f"you health is {health} would you like to use a kit y/n:>")
                if action == "y":
                    print("from the invatory read out you only have one small kit press 1 to select it")
                    action = input("""press 1 for small kit
                                    press 2 for medium kit
                                    press 3 for large kit
                                    press 4 for mini hospital
                                    press ext to exit
                                    :>""")
                    if action == "1":
                        if small_kit > 0:
                            health += settings.smallkit["health"]
                            small_kit -= 1
                            print("consumed kit health is now", health) 
                        else:
                            print("choose another kit")
                    if action == "2":
                        if medium_kit > 0:
                            health += settings.mediumkit[health]
                            medium_kit -= 1
                            print("consumed kit health is now", health) 
                        else:
                            print("choose another kit")
                    if action == "3":
                        if large_kit > 0:
                            health += settings.largekit[health]
                            large_kit -= 1 
                            print("consumed kit health is now", health)
                        else:
                            print("choose another kit")
                    if action == "4":
                        if medium_kit > 0:
                            health += settings.minihospital[health]
                            mini_hospital -= 1
                            print("consumed kit health is now", health) 
                        else:
                            print("choose another kit")
                    if action == "ext":
                        print("canceling")
                    print("you are out of kits and have reached max health if after battle be careful to select your kit wisely for any extra health after 200 will be droped and not applied press n")
                elif action == "n":
                    break
        input("now that your at full health proceed to next room press W")
        input("you moved to the next room a ASSD(automated security shock drone) is waiting for you press r to try to run past it or a to attack (press r)")
        print("you moved to the next room")
        input("press w to walk or e to check invatory press w")
        input("you moved to the next room a ASSD(automated security shock drone) is waiting for you press r to try to run past it or a to attack (press r)")
        enemy_damage = random.randint(settings.assddrone["damage-low"],settings.assddrone["damage-high"])
        print(f"while running the enemy caught you and delt {enemy_damage} damage")
        health -= enemy_damage
        enemy_health = settings.assddrone["health"]

        while True:
            extra = random.randint(3, 10)
            input("press a to attack or e to change weapons your current weapon is tesla stick press a")
            damage = settings.teslastick["damage"] + extra
            enemy_health -= damage
            print(f"you dealt {damage} damage plus {extra} extra, enemy health is now {enemy_health}")

            if enemy_health <= 0:
                print("defeated enemy")
                print("you picked up medium health kit")
                print("sometimes after killing an enemy, you get ammo or health from the drop")
                medium_kit += 1
                break
            else:
                enemy_damage = random.randint(settings.assddrone["damage-low"], settings.assddrone["damage-high"])
                health -= enemy_damage
                print(f"enemy dealt {enemy_damage} damage, your health is now {health}")

                if health <= 0:
                    print("you died")
                    break
        print("congrats you should be able to figue it out from here")
        break
        

            

        
        
            



    

#driver
for x in range(5):
    print("")
print("""you wake up on the cold concrete ground your not sure how you got here your in a room with grey concrete/metal walls
       there is one window in the room you look out and can tell your in some type of tower high above the clouds you leave
       the room through the one open door in hopes of finding a way down on your way out of the room you find a stick laying on the ground
       with a copper coil on top and a red button on the side you pick up the stick and push the botton electrical arcs start inmeting from
       the coil your not sure what your run into on your jounrey down but a weapon might help""")
t = input("would you like to read a turtoial y/n:>")
if t == "y":
    turtoial()
print("starting game")
game()
