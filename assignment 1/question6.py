# WRITE A PROGRAM TO FIND THE:
# a) THE AREA OF A CIRCLE
# c) THE AREA OF A SQUARE
# b) THE AREA OF A RECTANGLE

inpshape = input("please enter the shape of which you want to find the area of : ")
shape = inpshape.lower()
if shape == "square":
    side_length = int(input("please enter the length of the side of square : "))
elif shape == "rectangle":
    length = int(input("enter the lenght of the rectangle : "))
    width = int(input("enter the width of the rectangle : "))
elif shape == "circle":
    radious = int(input("please enter the radious of the circle : "))
else:
    print("please enter a shape from these shape : SQUARE or RECTANGLE or CIRCLE")


if shape == "square":
    area = side_length * side_length
    print("the area of the square is : ", area)
elif shape == "rectangle":
    area = length * width
    print("the area of the rectangle is : ", area)
elif shape == "circle":
    area = 3.14 * radious * radious
    print("the area of the circle is : ", area)
else:
    print("please reenter the shape you want to find the area of")