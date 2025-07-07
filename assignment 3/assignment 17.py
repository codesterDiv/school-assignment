'''
WAP to swap the string as shown(hint use slice) abc  -> xyz; abz -> xyc
'''


def swap_string(s):
    result = ''
    for c in s:
        if 'a' <= c <= 'z':
            result += chr(ord('x') + (ord(c) - ord('a')) % 3)
        else:
            result += c
    return result

# Example usage
print(swap_string('abc'))  # xyz
print(swap_string('abz'))  # xyc