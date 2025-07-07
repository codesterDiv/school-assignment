# print(" ASSIGNMENT 4: W.A.P. TO ACCEPT A NUMBER AND CHECK IF THE NUMBER IS POSITIVE OR NEGATIVE")
def num_chk2(number1):
    if number1 > 0:
        print(number1, "is a positive number")
    else:
        print(number1, "is a negative number")


number1 = int(input("enter the number : "))
num_chk2(number1)