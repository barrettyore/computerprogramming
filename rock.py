play1 = input("r,p,or s:>")
for i in range (500):
    print("")
play2 = input("r,p,or s:>")
if play1 == play2:
    print("tie")
elif play1 == "r" and play2  == "s":
    print("play1 won")
elif play1 == "r" and play2  == "p":
    print("play2 won")
elif play1 == "p" and play2  == "r":
    print("play1 won")
elif play1 == "p" and play2  == "s":
    print("play2 won")
elif play1 == "s" and play2  == "r":
    print("play2 won")
elif play1 == "s" and play2  == "p":
    print("play1 won")
else:
    print("unown input:>")
