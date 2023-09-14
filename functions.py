#name
def print_name(name):
    print(name)

#phrase
def phrase():
    global text
    text = " to watch cartoons"
phrase()
print(f"i want{text}")
#input
def user_print():
    print(input("type anything here:>"))
user_print()
#filter
listy = ["cat","dog","birb","fosh"]
def filtery(x):
  if x == "cat":
    return True
  else:
    return False

filter_function = filter(filtery, listy)

for x in filter_function:
  print(x)
#list
x = "i want to build a cat"
y = list(x)
print(y)
#map
def mappo(x):
   return x + "ito"

y = map(mappo, ("burr","mosqu","incog"))

print(list(y))
#range
for x in range(1,10):
   print(x)
#sort
listy = ['s', 'e', 'c', 'o', 'n', 'd']
print(sorted(listy))
#int
print(int("8576309"))
#string
print(str(104.36))