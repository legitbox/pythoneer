words = input("please input the strings, seperated by spaces: ") # we ask the user to input the strings

words_split = words.split() # we split the words

if len(words) == 0:
    print("Error: emty string") # error handling if the string is emty
else:
    print("Warning: string detected, continuing")
    longest_word = 0 # longest word search module
    for word in words_split:
        if len(word) > longest_word:
            longest_word = len(word)
            the_word = word
            
    shortest_word = len(the_word) # shortest word search module
    for sword in words_split:
        if len(sword) < shortest_word:
            shortest_word = len(sword)
            thes_word = sword

            
print("the longest word is: ", the_word, ", and the shortest is: ", thes_word) # we print out the word that we got in the search module
            