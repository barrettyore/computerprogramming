#varibles
x=0
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
                elif x%3 == 0:
                    print("fizz")
                elif x%5 == 0:
                    print("buzz")
                else:
                    print(x)
                x += 1

        else:
            print("PRIME")
            x += 1
    else:
        x += 1
