def convertName(string):
    res = ""
    for c in string:
        if c == ' ':
            res += '_'
        else:
            res += c
    return res



string = "Convert Sorted List to Binary Search Tree"
print(convertName(string))
