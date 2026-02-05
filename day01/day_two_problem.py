"""Given a string s, return the index of the first non-repeating character.
If no such character exists, return -1 """

def index_return(s):
    freq={}
    for char in s:
        freq[char]=freq.get(char,0)+1

    for index,char in enumerate(s):
        if freq[char]==1:
            return index
    return -1


if __name__=="__main__":
    s = input("Enter a string: \n")
    print(index_return(s))