import sys
from colorama import init, Style

# a) THE AREA OF A CIRCLE
# c) THE AREA OF A SQUARE
# b) THE AREA OF A RECTANGLE

def area_of_shape():
    if shape == "circle":
        area = (radious**2)*22/7
    elif shape == "rectangle":
        area = length*width
    else:
        area = side_length**2
    print(area)




inpshape = input("please enter the shape of which you want to find the are of : ")
shape = inpshape.lower()
if shape == "square":
    side_length = int(input("please enter the length of the side of square : "))
elif shape == "rectangle":
    length = int(input("enter the lenght of the rectangle : "))
    width = int(input("enter the width of the rectangle : "))
elif shape == "circle":
    radious = int(input("please enter the radious of the circle : "))
else:
    print("please enter a shape from these shape : ", f"{Style.BRIGHT}SQUARE or RECTANGLE or CIRCLE{Style.RESET_ALL}")

    sys.exit()


area_of_shape()