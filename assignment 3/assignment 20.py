thestr = "this is a test"
inputstr = input("Enter interger: ")
inputint = int(inputstr)
teststr = thestr
while inputint > 0:
    teststr = teststr[1:-1]
    inputint -= 1
testbool = 't' in teststr
print(thestr)
print(teststr)
print(testbool)
print(inputint)