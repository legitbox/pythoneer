# inputs the string to count
strin = input("please input the string to measure: ")

strin_words = strin.split()
strin_no_space = strin.replace(" ", "")


strin_len = len(strin_no_space)
strin_word_len = len(strin_words)

print("the lenght of the string is: ", strin_len)
print("the count of the words is: ", strin_word_len)
