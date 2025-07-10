inputstr = input("Enter string: ")
bigint = 0
smallint = 0
otherint = 0
for x in inputstr:
    if x>= 'a' and x <= 'm':
        smallint += 1
    elif x >= 'm' and x <= 'z':
        bigint += 1
    else:
        otherint += 1

print(bigint)
print(smallint)
print(otherint)
print(inputstr.isdigit())