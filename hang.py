import random

#funcs

def get_word():
    word_list = []
    f = open("sowpods.txt", "r")
    for x in f:
        word_list.append(x)
    y = random.choice(word_list)
    print(y)#debug
    return(y)

def game():
    empty = []
    incorrect = []
    lives = 6
    print(word)
    for x in range(len(word)):
        empty.append("_")
    print(empty)#debug delete later
    fin = False
    while lives > 0 or fin != False:
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
                        print(f"you did it you did it you did it the word was{word_og}")
                        fin = True
                        break
                print(empty)
            else: 
                print("wrong letter try again")
                incorrect.append(guessed)
                lives -= 1
                print(lives)#change to correct art type latter

        
        
        
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

#driver
print("welcome to hang man")
dead()
print("getting word")#debug
word_og = get_word()
word = list(word_og)
word.pop()
game()