#life is pain life is mirey all i want to do is go home walk my dog pet my cat eat icecream wake up tommorow and play microsoft flight simulator x steam edition for 83 hours
print("Welcome to the flows")
word_og = "kittens"
word = list(word_og)

empty = []
for x in range(len(word)):
    empty.append("_")

fin = True
while fin:
    guessed = input("type you guess letter here:>")
    
    if len(guessed) == 1:
        
        if guessed in word:
            for x in range(len(word)):
            

                indices = []

                #check exteince of life in barrett please i think i died



                    #grap index of letter

                for x in range(len(word)):
                    if word[x] == guessed:
                        indices.append(x)
                        # print(indices)
                        
                        

                    #replace blank with letter at index

                for x in range(len(indices)):
                    empty[indices[x]] = guessed
                    

                    #check if user won
                
                if empty == word:
                    print("you did it you did it you did it the word was")
                    fin = False
                    break
            print(empty)
        else: 
            print("wrong letter try again")

        
        
        
    else:
        print("only one letter at a time please")
    
print(word_og)