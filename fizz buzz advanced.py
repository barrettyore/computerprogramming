#varibles
x=0 
fizz = 0
buzz = 0
fizz_buzz = 0
final_count = []
sn = int(input("special number here (1-10 only):>"))
sw = input("replace word here:>")
#count
while x<=100:
    # If given number is greater than 1
    if x > 1:
        for i in range(2, int(x/2)+1):
            if (x % i) == 0:
                if x%sn == 0:
                    print(sw)
                
                elif x%3 == 0 and x%5 == 0:
                    print("fizz buzz")
                    fizz_buzz += 1
                elif x%3 == 0:
                    print("fizz")
                    fizz += 1
                elif x%5 == 0:
                    print("buzz")
                    buzz += 1
                else:
                    print(x)
                x += 1

        else:
            print("PRIME")
            x += 1
    else:
        x += 1
