def convertName(string):
    res = ""
    for c in string:
        if c == ' ':
            res += '_'
        else:
            res += c
    return res


string = "Minimum Absolute Difference in BST"
print(convertName(string))
