
try:
    numlist = input("input a list of numbers that are separated by a space: ")
    numlist_split = numlist.split()
    numlist_len = len(numlist_split)
    print("list count: ", numlist_len)
    print(numlist_split, "test complete, continuing operation")
    numlist_split = [int(num) for num in numlist_split]
    print("conversion complete, continuing")
    numlist_average = sum(numlist_split) / numlist_len
    print("the average of the numbers is: ", round(numlist_average, 2))
except:
    print("operation failure detected, please try again!")