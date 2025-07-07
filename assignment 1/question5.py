# print(" ASSIGNMENT 5: W.A.P. TO MAKE A SIMPLE CALCULATOR")

def calculator(operator, number1, number2):
    if operator == "+":
        result = number1 + number2
        print("sum of the 2 numbers is : ", result)
    elif operator == "-":
        if number1 > number2:
            result = number1-number2
        else:
            result = number2-number1
        print(result)
    elif operator == "*":
        result = number1*number2
        print(result)
    elif operator == "/":
        if number1 > number2:
            result = number1/number2
        else:
            result = number2/number1
        print(result)
    else:
        print("please reenter the number...")


operator = input("please enter the operator you want to use : ")
number1 = int(input("enter the first number : "))
number2 = int(input("please enter the second number : "))
calculator(operator, number1, number2)