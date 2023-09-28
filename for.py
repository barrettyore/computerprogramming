#word
word = "paradigm"
for i in word:
    print(i)
#range
for i in range(0,7):
    print(i)
#list
AnimalList = ['Cat','Dog','Tiger','Cow']
for i in AnimalList:
    print(i)
#else
flowers = ['Jasmine','Lotus','Rose','Sunflower']
x = 0
for i in flowers:
    if x < 3:
        print(i)
        x += 1
    else:
        print("done")
#nested
list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']
for i in list1:
    for n in list2:
        print(i,n)
#break
vehicles = ['Car','Cycle','Bus','Tempo']
for i in vehicles:
    if i == "bus":
        break
    else:
        print(i)
#continue
vehicles = ['Car','Cycle','Bus','Tempo']
for i in vehicles:
    if i == "bus":
        continue
    else:
        print(i)
#count
numbers = [12,3,56,67,89,90]
count = 0
x = 0
for i in numbers:
    x += numbers[count]
    count += 1
print(x)
#multibles
numbers = [2,5,6,10,15,20,25]
for i in numbers:
    count = i
    while count > 0:
        count -= 5
        if count == 0:
            print(i)
        elif count < 0:
            break
#list
list1 = ['Mango','Banana','Orange']
list2 = []
for i in list1:
    list2.append(i)
print(list2)
#max
current = 0
new = 0
numbers = [1,4,50,80,12]
for i in numbers:
    new = i
    if new > current:
        current = new
print(current)
#min
numbers = [1,4,50,80,12]
current = 99999
new = 0
numbers = [1,4,50,80,12]
for i in numbers:
    new = i
    if new < current:
        current = new
print(current)
#sort 
numbers = [1,4,50,80,12]
current = numbers[1]
new = 0
numbers = [1,4,50,80,12]
numbers.sort()
list2 = []
for i in numbers: 
    list2.append(i)
print(list2)
#sort in revese
numbers = [1,4,50,80,12]
numbers.sort()
numbers.reverse()
list1 = []
for i in range(len(numbers)):
    list1.append(i)
#multibles range 3
list1 = [3]
current = 3
for i in range(5):
    list1.append(current + 3)
    current += 3
print(list1)
#multiples range 5
list1 = [5]
current = 5
for i in range(2):
    list1.append(current + 5)
    current += 5
print(list1)
#count revese
max = 10
for i in range(10):
    print(max)
    max -= 1