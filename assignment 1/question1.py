# QUESTION 1: FIND MAXIMUM OF 2 NUMBERS
def max(a, b):
    if a > b:
        print(a, " is greater than", b)
    else:
        print(b, " is greater than", a)
no1 = int(input("enter first number : "))
no2 = int(input("enter the second numer : "))
max(no1, no2)
