# print(" ASSIGNMENT 7: W.A.P. TO ACCEPT A CHARACTER AND CHECK IF IT IS UPPERCASE OR LOWERCASE")



char = input("please enter any character (uppercase or lowercase) : ")

if char.islower():
    print("the entered character is lower cased")
elif char.isupper():
    print("the entered character is upper cased")
else:
    print("please enter a character (alphabet)")