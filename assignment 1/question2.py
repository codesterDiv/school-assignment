# QUESTION 2: FIND MAXIMUM OF 3 NUMBERS

num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number : "))
num3 = int(input("enter the third number : "))

if num1 > num2 and num1 > num3:
    print(num1, " is greater than" , num2 , "and", num3 )
elif num2 > num1 and num2 > num3:
    print(num2, " is greater than" , num1 , "and", num3 )
else:
    print(num3, " is greater than" , num1 , "and", num2 )
