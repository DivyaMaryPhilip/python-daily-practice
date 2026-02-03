"""
    Return the first character in string s that does not repeat.
    If none exists, return None.
    """


def first_non_rep_char(s):
    freq={}
    for char in s:
        freq[char]=freq.get(char,0)+1

    for char in s:
        if freq[char] == 1:
            return char
    return None


if __name__=="__main__":
    s = input("Enter a string: \n")
    print(first_non_rep_char(s))















