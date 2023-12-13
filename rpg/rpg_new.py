#IMPORTS
import random
from settings import *

#varibles
global pulse_cartridge
pulse_cartridge = 1
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
invatory = ["small kit","medium kit","large kit","mini hospital","tesla stick",]
global weapons_inventory
global current_weapon_index
current_weapon_index = 0
weapons_inventory = ["tesla stick",]
global health
health = settings.MAX_HEALTH
global current_weapon
current_weapon = 0
global name 
name = ""
global enemys_encounterd
enemys_encounterd = 0
global enemy_list
enemy_list = ["AssdDrone"]
global matter_canister
matter_canister = 0

#game code

def encounter_enemy():
    global enemy_list
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


def change_weapon():
    global current_weapon_index

    print("Current weapons in inventory:")
    for index, weapon in enumerate(weapons_inventory):
        print(f"{index + 1}. {weapon}")

    # Get user input for the selected weapon
    while True:
        try:
            choice = int(input("Enter the number of the weapon to switch to (0 to cancel): "))
            if 0 <= choice <= len(weapons_inventory):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Switch to the selected weapon
    if choice != 0:
        current_weapon_index = choice - 1
        print(f"You switched to {weapons_inventory[current_weapon_index]}.")
    else:
        print("Weapon change canceled.")

def check_inv():
    global small_kit
    global medium_kit
    global large_kit
    global mini_hospital
    global health
    print(F"{name}'s health is {health}")  
    print("pulse cartridge:", pulse_cartridge)
    print("matter canister:", matter_canister)

    for item in invatory:
        if item == "tesla stick":
            print(settings.teslastick)
        elif item == "tesla rifle":
            print(settings.teslarifle)
        elif item == "gravity disperser":
            print(settings.gravitydisperser)
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


def combat_loop(enemy_name, enemy_settings, weapon_settings,):
    global enemys_encounterd
    enemys_encounterd += 1 
    global current_weapon_index
    global current_weapon_settings
    global small_kit
    global medium_kit
    global large_kit
    global mini_hospital
    global pulse_cartridge
    global health
    global matter_canister
    enemy_health = enemy_settings["health"]
    print(f"you encourted a {enemy_name}({enemy_settings['name']}) with {enemy_health} health")
    while health > 0 and enemy_health > 0:
        action = input("Press 'a' to attack, 'e' to escape, or 'c' to change weapon: > ")

        if action == 'a':
            # Attack with the current weapon
            current_weapon_name = weapons_inventory[current_weapon_index]
            print(current_weapon_name)
            current_weapon_settings = getattr(settings, current_weapon_name.replace(" ", "").lower(), None)


            if current_weapon_settings is not None:
                extra = random.randint(3, 10)

                if 'damage' in current_weapon_settings:
                    if enemy_name == "asd":
                        chance = random.randint(1,3)
                        if chance == 1:
                            print("the stealth drone activated its cloacker you took a blind shot and missed")
                        else:
                            if current_weapon_name == "pulse pistol" and pulse_cartridge < 1:
                                print("you have no ammo left and didnt fire")
                            elif current_weapon_name == "gravity disperser" and matter_canister < 1:
                                print("you have no ammo left and didnt fire")
                            else:
                                if current_weapon_settings["type"] == enemy_settings["type"]:
                                    damage = current_weapon_settings["damage"] + extra + 10
                                    enemy_health -= damage
                                    print(f"You dealt {damage} damage plus {extra} extra and 10 for same type bonus. Enemy health is now {enemy_health}.")
                                else:    
                                    damage = current_weapon_settings["damage"] + extra
                                    enemy_health -= damage
                                    print(f"You dealt {damage} damage plus {extra} extra. Enemy health is now {enemy_health}.")
                                if current_weapon_name == "gravity disperser":
                                    matter_canister -= 1 
                                    print(f"you have {matter_canister} matter canister's left")
                                    
                                if current_weapon_name == "pulse pistol":
                                    pulse_cartridge -= 1
                                    print(f"you have {pulse_cartridge} pulse cartidge's left")
                    else:
                        if current_weapon_name == "pulse pistol" and pulse_cartridge < 1:
                            print("you have no ammo left and didnt fire")
                        elif current_weapon_name == "gravity disperser" and matter_canister < 1:
                            print("you have no ammo left and didnt fire")
                        else:
                            if current_weapon_settings["type"] == enemy_settings["type"]:
                                damage = current_weapon_settings["damage"] + extra + 10
                                enemy_health -= damage
                                print(f"You dealt {damage} damage plus {extra} extra and 10 for same type bonus. Enemy health is now {enemy_health}.")
                            else:
                                damage = current_weapon_settings["damage"] + extra
                                enemy_health -= damage
                                print(f"You dealt {damage} damage plus {extra} extra. Enemy health is now {enemy_health}.")
                            if current_weapon_name == "gravity disperser":
                                matter_canister -= 1 
                                print(f"you have {matter_canister} matter canister's left")
                            if current_weapon_name == "pulse pistol":
                                pulse_cartridge -= 1
                                print(f"you have {pulse_cartridge} pulse cartidge's left")
                    if enemy_health <= 0:
                        print("You defeated the enemy!")
                        chance = random.randint(1, 5)
                        if chance == 1:
                            print("You picked up 1 small kit.")
                            small_kit += 1
                        elif chance == 2:
                            print("You picked up 1 medium kit.")
                            medium_kit += 1
                        elif chance == 3:
                            print("You picked up 1 large kit.")
                            large_kit += 1
                        elif chance == 4:
                            print("You picked up 1 mini hospital.")
                            mini_hospital += 1
                        elif chance == 5:
                            chance = random.randint(1,3)
                            if chance == 1:
                                if "pulse pistol" in weapons_inventory:
                                    pulse_cartridge += 5
                                    print("you picked up 5 pulse cartridge")
                            if chance == 2:
                                if "gravity disperser" in weapons_inventory:
                                    matter_canister += 5
                                    print("you have picked up 5 matter canister")
                            if chance == 3:
                                if "gravity disperser" in weapons_inventory:
                                    matter_canister += 5
                                    print("you have picked up 5 matter canister")
                                if "pulse pistol" in weapons_inventory:
                                    pulse_cartridge += 5
                                    print("you picked up 5 pulse cartridge")
                    else:
                        # Enemy's turn
                        enemy_damage = random.randint(enemy_settings["damage-low"], enemy_settings["damage-high"])
                        health -= enemy_damage
                        print(f"The enemy dealt {enemy_damage} damage. Your health is now {health}.")

                        if health <= 0:
                            if enemy_name == "AssdDrone":
                                print(f"{name} suffered a heart attack because of the shocks from a assddrone")
                            if enemy_name == "ald":
                                print(f"{name} was burnt by the laser of a ald")
                            if enemy_name == "walker":
                                print(f"{name} was stepped on by a walker")
                            if enemy_name == "asd":
                                print(f"{name} was lacerated by a asd")
                            if enemy_name == "at":
                                print(f"{name} was shot by a at")
                            break
            else:
                print(f"Error: 'damage' key not found in weapon settings for {current_weapon_name}")



        elif action == 'e':
            chance = random.randint(1,3)
            if chance == 1:
                print("You escaped from the enemy.")
                break
            else:
                print("the enemy has blocked you from running past")

        elif action == 'c':
            change_weapon()

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
    global name
    global current_weapon_index
    global enemys
    global pulse_cartridge
    global matter_canister
    # variables
    health = settings.MAX_HEALTH
    name = input("you're having trouble remembering your name, what is it: > ")

    # game
    print('new weapon unlocked "tesla stick"')

    while health > 0:  # Check if the player is still alive
        action = input("Press 'w' to walk or 'e' to check inventory: > ")

        if action == 'w':
            if random.randint(1, 4) == 1:
                if enemys_encounterd == 6:
                    enemy_list.append("ald")
                    weapons_inventory.append("tesla rifle")
                    invatory.append("tesla rifle")
                    print("in this new room a shiny copper object catches you eye you pick it up and observe your new weapon it has a grey and black metal stock with blue lights and a screen at the end of the stock instead of seeing a normal barrell there is a coil simmuler to that of your tesla stick you shoulder the rifle and pull the trigger the lights and screen change as the weapon starts makeing a loud high pitched wine the lights turn green and the screen reads pull trigger to second stage to fire you pull a loud crack sounds and the room lights up a bright blue has a huge electrical ark fires forward from the coil the sound and light is overwhelming and attracts the attention of a enemy from the next room get ready")
                    print('new weapon unlocked "tesla rifle"')
                if enemys_encounterd == 9:
                    enemy_list.append("asd")
                    weapons_inventory.append("plasma througher")
                    invatory.append("plasma througher")
                    print("in this new room a blue light catches your eye you look down and find what looks like a heavy rifle the gun has is long with a window that shows a faint glowing blue rod in a pool of water the gun is obvously ment to be hip hold sceince there is handels on the top at the back of the gun there is a hose leading to a back pack with some sort of liquid in it on the top of the gun there is a screen with a radation symbole and reactor status lights and numbers must be the glowing rod you thought to your self you dont know what the gun does yet but its obvousilly nucelar powerd the front of the gun fetrues a edf fan with vents along the side of the barrel on the front of the barrel there is six metal arms with cooper tips and a wire feeding into the guns side you bend down put on the back pack and hold the gun you push the trigger down the faint blue glow turns to a bright purple as a load roar climbs in pitch then the tiny fan speeds up fast enoguh to start pulling on your arms all of a sudden the copper tipes arms light up with arcs then CRACK the rooms lights up a bright white as a shower of plasma fleas from the end of the gun and setting the war sepreating the next room on fire the recoil was almost enoguh to kncok you down you release the trigger and the gun stops makeing a slow declaing hum as the plasma disapates the buring wall is now only ash and a stunned enemy is looking at you get ready ")
                    print('new weapon unlocked "plasma througher"')
                if enemys_encounterd == 14:
                    enemy_list.append("at")
                    weapons_inventory.append("gravity disperser")
                    invatory.append("gravity disperser")
                    print("it this new room a shiny metal catches you attention you bend down a pick up a rifle the rifle has a serious of windows with circutry glowing orange the barrel of the gun is in a weird cone shape with no actual opening that appears to be bending a tiny bit of light around it you aim it at the war and pull the trigger the shot sounds like an air valve opening when you shot instead of being pushed back by recoil it felt like you have been pulled forward the shot is travelling slow enough for you to see it however there is no actuall bullet instead you say a invisible distoration bending light as it travels before finnally hitting the war once it hits the distoration turns black and sucks in the sounding wall before disapearing with a loud poping sound the wall has a big chunk in the midle missing with the reamaing being bent and pulled in weird paterns holy #### was that a ####ing black hole you say aloud your voice attracted a enemy get ready ")
                    print("new weapon unlocked gravity disperser")
                    print("new ammo unlocked matter canister you have been given 5 shots")
                    matter_canister = 5
                if enemys_encounterd == 20:
                    enemy_list.append("walker")
                    weapons_inventory.append("pulse pistol")
                    invatory.append("pulse pistol")
                    pulse_cartridge = 5
                    print("it this new room a small metalic object catches your eye you pick it up its a small pistol with with what appears to be some type of speaker on the front you pick it up and pull the trigger the gun starts makeing a loud pulsing charging sound before release a thundress whomp and releasing a visable pressure wave distryoing the next wall the sound attracketed a enemy get ready")
                    print("new weapon unlocked pusle pistol")
                    print("new ammo unlocked pulse cartridge you have been given 5 shots")
                if enemys_encounterd == 30:
                    print(f"you are now on the ground floor and you see a door labled exit next to the door is a button labbled open you hit the button the door parcially opens revealing sun light through then it stops a voice comes over the speaker hello {name} are you really that stupid that you think we will just let you out of here than a sound wines up it sounds like a explosive you run away from the door but its to late the room explodes you and some of the walls get flong out side 50 feet in the air and just when you thought your adventure came to a end you hear a weird sound and time stops you cant move the explosion below is paused evrything is paused then a man in a red site seemingly walks out of the sky and talks to you he says well done {name} well done your battle for freedom was impressive so much so in fact i have decided to save you for some feture jobs you are not needed at the moment so i will keep in stasis untill ready the man then turns around and starts walking to where he came from then stops turns and says oh by the way {name} i took the liberty of reliving you of all of your weapons there were all private property anyways then man then precceds to continue walking and fades out and dissapears as easily has he appeared your inviorment fades to black it looks like your adventure is not over yet")
                    exit()
                    


                print(enemy_list)

                enemy_name, enemy_settings = encounter_enemy()
                in_combat = True
                combat_loop(enemy_name, enemy_settings, weapons_inventory)  # Pass weapons_inventory
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
    print("restart game to play")
    exit()
print("starting game")
game()
