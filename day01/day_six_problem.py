"""Given a string s, return the first character whose frequency is greater than 1 and whose second occurrence appears earliest in the string."""

def returnchar(s):
    myset = set()
    for char in s:
        if char in myset:
            return char
        myset.add(char)
    return None

if __name__ == "__main__":
    s = "eddabbcd"
    print(returnchar(s))

