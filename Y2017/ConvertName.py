def convertName(string):
    res = ""
    for c in string:
        if c == ' ':
            res += '_'
        else:
            res += c
    return res



string = "Maximum XOR of Two Numbers in an Array"
print(convertName(string))
