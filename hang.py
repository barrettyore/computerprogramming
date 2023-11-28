import random

#funcs

def get_word():
    word_list = []
    f = open("sowpods.txt", "r")
    for x in f:
        word_list.append(x)
    y = random.choice(word_list)
    # print(y)#debug
    return(y)

def game():
    empty = []
    incorrect = []
    global lives
    lives = 6
    # print(word)
    for x in range(len(word)):
        empty.append("_")
    # print(empty)#debug delete later
    fin = False
    while lives > 0 and fin == False:
        print(f"you current already guessed letters are...{incorrect}")
        guessed = input("type you guess letter here:>")
        if len(guessed) == 1:
            if guessed in incorrect:
                print("letter already guessed try again")
            elif guessed in word:
                for x in range(len(word)):
                
                    
                    indices = []

                    #check exteince of life in barrett please i think i died

                    

                        #grap index of letter

                    for x in range(len(word)):
                        if word[x] == guessed:
                            indices.append(x)
                            
                            
                            

                        #replace blank with letter at index

                    for x in range(len(indices)):
                        empty[indices[x]] = guessed
                        

                        #check if user won

                    if empty == word:
                        fin = True
                        e()
                        break
                print(empty)
                if empty == word:
                    print(f"you did it you did it you did it the word was {word_og}")
            else: 
                print("wrong letter try again")
                incorrect.append(guessed)
                lives -= 1
                if lives == 5:
                    d1()
                elif lives == 4:
                    d2()
                elif lives == 3:
                    d3()
                elif lives == 2:
                    d4()
                elif lives == 1:
                    d5()
                else:
                    dead()

        
        
        
        else:
                print("only one letter at a time please")
    




#art
def dead():
    print("	|-------|")
    print("	|       |")
    print("	o       |")
    print("       -|-	|")
    print("       / \	|")
    print("                |")
    print("       _________⊥__________")

def d1():
    print("""	|-------|
	|	|      
	o	|
       		|
        	|
		|
________________⊥______________________
""")

def d2():
    print("""	|-------|
	|	|      
	o	|
        |	|
       		|
		|
________________⊥______________________""")

def d3():
    print("""	|-------|
	|	|      
	o	|
       -|	|
       		|
		|
________________⊥______________________""")

def d4():
    print("""	|-------|
	|	|      
	o	|
       -|-	|
       		|
		|
________________⊥______________________""")

def d5():
    print("""	|-------|
	|	|      
	o	|
       -|-	|
       / 	|
		|
________________⊥______________________
""")

def e():
    print("""	|-------|
	|	|      
		|
       		|
       		|
		|
________________⊥______________________
""")
def a():
    print("""      	     thank you for playing!	
	o	
       -|-	
       / \	
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾""")

#driver
#art test
#dead
# dead()
# d1()
# d2()
# d3()
# d4()
# d5()
# e()
# a()


print("welcome to hang man")
dead()
print("getting word")#debug
word_og = get_word()
word = list(word_og)
word.pop()
game()
if lives == 0:
    print(f"you failed the word was {word_og}")
while True:
    again = input("do you want to play again y/n:>")
    if again == "y":
        print("getting word")#debug
        word_og = get_word()
        word = list(word_og)
        word.pop()
        game()
        if lives == 0:
            print(f"you failed the word was {word_og}")
            
    else:
        a()
        break