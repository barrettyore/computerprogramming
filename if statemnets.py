#rember adis from last year
#salary
import time
print("hello user and welcome back to the A.D.I.S.")
print("hello and welcome to your auomated quistionner for totally ok not questionable soft ware development company ")
print("im A.D.I.S (automated documanting interveiw system) your questionner guid for the your potientall salory raise")
input("press enter whenn ready:>")
print("A.D.I.S intallizing__:>")
time.sleep(.25)
print("A.D.I.S intallized__:>")
name_question = input("what is you name...")
year_question = int(input("how many years did you work with us..."))
if year_question >= 5:
    salary_question = int(input("what is you current salary..."))
    print(f"your new salary after next pay check will by {salary_question+ (0.05 * salary_question)}")
    time.sleep(0.25)
    print("A.D.I.S shutdown succesfull__:>")
else:
    print("im sorry but you have not worked with us long enough__:>")
    time.sleep(0.25)
    print("A.D.I.S deleted submission__:>")
    time.sleep(0.25)
    print("A.D.I.S !TERMINATE__:>")
    time.sleep(0.25)
    print("A.D.I.S succesfully terminated__:>")
#square
width = int(input("width number here:>"))
height = int(input("height number here:>"))
if height == width:
    print("this is a square")
else:
    print("this is a rectangle")
#greater than
num1 = int(input("num1:>"))
num2 = int(input("num2:>"))
if num1 > num2:
    print("num1 is bigger")
else:
    print("num2 is greater")
#list compare
list1 = []
list1.append(input("age1:>"))
list1.append(input("age2:>"))
list1.append(input("age3:>"))
list1.sort()
print(list1[0],list1[2])
#collage
#sorry i lost my mind here
class1 = int(input("how many classsses did you haveee:>"))
class2 = int(input("how many of those classes did you actually attend you free loader:>"))
if (100 * class2/class1) < 75:
    print("not enough intendance")
else:
    print("you can take the test")
