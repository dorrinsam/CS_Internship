def is_isogram(string):
    l_str = string.lower()
    str = l_str.replace(" ", "").replace("-", "")

    if len(str) == len(set(str)):
        return True

    return False