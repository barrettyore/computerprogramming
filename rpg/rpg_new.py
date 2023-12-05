#IMPORTS
import random
from settings import *

#varibles
pulse_cartridge = 20
global small_kit
global medium_kit
global large_kit
global mini_hospital
small_kit = 1
medium_kit = 0
large_kit = 0
mini_hospital = 0
global invatory
invatory = ["pulse pistol","tesla stick","tesla rifle","small kit"]
global health
health = settings.MAX_HEALTH

#game code
def check_inv():
    global small_kit
    global medium_kit
    global large_kit
    global mini_hospital
    global health  
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
    if small_kit or medium_kit or large_kit or mini_hospital > 1:
        while True:
            action = input("would you like to use a kit y/n:>")
            if action == "y":
                action = input("""press 1 for small kit
                            press 2 for medium kit
                            press 3 for large kit
                            press 4 for mini hospital""")
                if action == "1":
                    if small_kit > 0:
                        health =+ settings.smallkit[health]
                        small_kit =- 1 
                    else:
                        print("choose another kit")
                if action == "2":
                    if medium_kit > 0:
                        health =+ settings.mediumkit[health]
                        medium_kit =- 1 
                    else:
                        print("choose another kit")
                if action == "3":
                    if large_kit > 0:
                        health =+ settings.largekit[health]
                        large_kit =- 1 
                    else:
                        print("choose another kit")
                if action == "4":
                    if medium_kit > 0:
                        health =+ settings.minihospital[health]
                        mini_hospital =- 1 
                    else:
                        print("choose another kit")

            elif action == "n":
                break

def game():
    global small_kit
    global medium_kit
    global large_kit
    global mini_hospital
    global health 
    invatory = ["telsa stick"]
    #varibles
    health = settings.MAX_HEALTH
    name = input("your having trouble remebering your name, what is it:>")

    #game
    print('new weapon "tesla stick')

def turtoial():
    
    
    print("welcome to the turtoial")
    print("in this game you will walk between rooms while running into enemys and managing your weapons and invetory")
    print("starting scenario")
    while True:
        input("every turn of the game you will see a prompt like the following <press w to walk or press e to check invatory> presss w:>")
        print("you walked to the next room")
        input("every turn of the game you will see a prompt like the following <press w to walk or press e to check invatory> presss e:>")
        check_inv()
        
        
            



    

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