'''
write a program to convert string to list
write a program to count the number of words in a string
'''


# Convert string to list
input_string = "Hello world this is a test"
string_list = input_string.split()
print("List:", string_list)

# Count the number of words in a string
word_count = len(string_list)
print("Number of words:", word_count)