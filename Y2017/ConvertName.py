def convertName(string):
    res = ""
    for c in string:
        if c == ' ':
            res += '_'
        else:
            res += c
    return res


string = "Read N Characters Given Read4"
print(convertName(string))
