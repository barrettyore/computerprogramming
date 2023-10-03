sequence = int(input("how long do you want the sequence to run for:>"))
sequence -= 2
orgin = 2 
current = 1
print(current)
print(current)
for i in range(sequence):
    print(orgin)
    old_orgin = orgin
    orgin += current
    current = old_orgin
 