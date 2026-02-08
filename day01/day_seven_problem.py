
"""Given a string s, return the length of the longest substring without repeating characters."""

def longestuniquesubstr(s):
    max_len = 0
    left=0
    myset = set()
    for right in range(len(s)):
        while s[right] in myset:
            myset.remove(s[left])
            left+=1
        myset.add(s[right])
        max_len = max(max_len,right-left+1)
    print(max_len)

if __name__=="__main__":
    s="pwwkew"
    longestuniquesubstr(s)
