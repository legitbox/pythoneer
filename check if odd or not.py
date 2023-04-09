try:
    num = input("please input a number to check if it's odd or not: ")
    num = int(num)
    if num % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")
except:
    print("operation failure, please input a valid number!!!")