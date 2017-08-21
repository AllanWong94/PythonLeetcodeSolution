def convertName(string):
    res = ""
    for c in string:
        if c == ' ':
            res += '_'
        else:
            res += c
    return res


string = "Minimum Index Sum of Two Lists"
print(convertName(string))
