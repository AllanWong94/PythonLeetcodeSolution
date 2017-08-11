def convertName(string):
    res = ""
    for c in string:
        if c == ' ':
            res += '_'
        else:
            res += c
    return res


string = "Find Mode in Binary Search Tree"
print(convertName(string))
