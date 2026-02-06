"""Given a string s, find the first character that appears exactly twice.
Return the character itself.
If no such character exists, return None."""

def first_char_exactly_twice(s):
    freq={}
    for char in s:
        freq[char] = freq.get(char,0)+1

    for everychar in s:
        if freq[everychar]==2:
            return everychar
    return None

if __name__ == "__main__":
    s = "avail"
    print(first_char_exactly_twice(s))