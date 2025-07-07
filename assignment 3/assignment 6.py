'''
write a program to search for a word in a string. if it exists print "found" if it does not exist print "not found".
'''


input_string = input("Enter a string: ")
search_word = input("Enter the word to search: ")

if search_word in input_string.split():
    print("found")
else:
    print("not found")