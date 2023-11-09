import random
word_list = []
f = open("sowpods.txt", "r")
for x in f:
  word_list.append(x)
print(random.choice(word_list))
