print("Welcome to the flows")
word_og = "kittens"
word = list(word_og)
print(word) #debug delete later
empty = []
for x in range(len(word)):
    empty.append("_")
print(empty)#debug delete later
fin = True
while fin:
    guessed = input("type you guess letter here:>")
    if len(guessed) == 1:
        if guessed in word:
            for x in range(len(word)):
            
                print(word[x],"index",x)#debug delete later
                indices = []

                #check exteince of life in barrett please i think i died

                

                    #grap index of letter

                for x in range(len(word)):
                    if word[x] == guessed:
                        indices.append(x)
                        print(indices)
                        
                        

                    #replace blank with letter at index

                for x in range(len(indices)):
                    empty[indices[x]] = guessed
                    print(empty)

                    #check if user won

                if empty == word:
                    print("you did it you did it you did it the word was")
                    fin = False
                    break
            
        else: 
            print("wrong letter try again")

        
        
        
    else:
        print("only one letter at a time please")
    
print(word_og)