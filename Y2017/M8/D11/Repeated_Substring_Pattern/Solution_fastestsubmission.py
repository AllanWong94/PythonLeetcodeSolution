
def repeatedSubstringPattern(str):
    """
    :type str: str
    :rtype: bool
    """
    if not str:
        return False

    ss = (str + str)[1:-1]
    return ss.find(str) != -1

print(repeatedSubstringPattern('abab'))