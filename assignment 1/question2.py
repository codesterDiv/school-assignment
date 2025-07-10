# QUESTION 2: FIND MAXIMUM OF 3 NUMBERS
def max2(a, b, c):
    if a > b and a > c:
        print(a, " is greater than" , b , "and", c )
    elif b > a and b > c:
        print(b, " is greater than" , a , "and", c )
    else:
        print(c, " is greater than" , a , "and", b )
num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number : "))
num3 = int(input("enter the third number : "))

max2(num1, num2, num3)
