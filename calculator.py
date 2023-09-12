nu1 = 0.0
nu2 = 0.0
nu1 = input("please insert first number here:>")
nu2 = input("please insert second number here:>")
float(nu1)
float(nu2)
action = input("please type wanted function or help for list of commands:>")

def add(nu1,nu2):
    print(f"{nu1} added by {nu2} is enqual to {float(nu1)+float(nu2)}")

def sub(nu1,nu2):
        print(f"{nu1} subtracted by {nu2} is enqual to {float(nu1)-float(nu2)}")

def div(nu1,nu2):
    print(f"{nu1} divided by {nu2} is enqual to {float(nu1)/float(nu2)}")

def mul(nu1,nu2):
    print(f"{nu1} multiplyed by {nu2} is enqual to {float(nu1)*float(nu2)}")

def mod(nu1,nu2):
    print(f"{nu1} modded by {nu2} is enqual to {float(nu1)%float(nu2)}")

def help():
    print("type add to do addition, type sub to do subtraction, type div to do divison, type mul for multiplaction, type mod for modulotion?:>")

if action == "add":
    add(nu1,nu2)
elif action == "sub":
    sub(nu1,nu2)
elif action == "div":
    div(nu1,nu2)
elif action == "mul":
    mul(nu1,nu2)
elif action == "mod":
    mod(nu1,nu2)
elif action == "help":
    help()
else:
    print("unsurported input")
    