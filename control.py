#break
import random
while True:
    x = random.randint(1,3)
    print(x)
    if x == 3:
        break
#for 
x = "this is a very long statement and probably a waste of time to type all of this but it can be fun so enjoy this fun fact: L.A.S.E.R. is an acryonem standing for LIGHT AMPLICATION STIMULATED by EMMISIION of RADATION"
for i in range(len(x)):
    print("why did i type this")
#while
x = 0
while x < 10:
    x += 1
    print(x)
#nested loop
for i in range(1,10):
    print("outer")
    for i in range(1,10):
        print("inner")
#nested if 
x = 3 
y = 5
if x == 3:
    print("wahoo")
    if x == 5:
        print("waaaho")
#met condition
cat_color = "black"
if cat_color == "black":
    print("my irl cat is black")
#failed condition
time_of_day_i_wrote_this = "day"
if time_of_day_i_wrote_this == "night":
    print("late night huh?")
#iterate 
x = ["cat", "dog", "bird"]
y = random.randint(0,2)
print(x[y])

#complex statement
x = False
y = True
if x and y:
    print("sample message")

#exit condition
import random
while True:
    x = random.randint(1,3)
    print(x)
    if x == 3:
        break

#infite loop
while True:
    print("you gonna be tired of this message")