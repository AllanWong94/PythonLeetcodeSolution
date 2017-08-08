def convertName(string):
    res = ""
    for c in string:
        if c == ' ':
            res += '_'
        else:
            res += c
    return res


string = "Remove Nth Node From End of List"
print(convertName(string))
