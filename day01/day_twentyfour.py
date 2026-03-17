"""Given a string s, find the length of the 
longest substring without repeating characters."""

def longestsubstr(s):
    freq = {}
    left = 0 
    max_len = 0

    for right in range(len(s)):
        freq[s[right]]=freq.get(s[right],0)+1

        while freq[s[right]]>1:
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1

        max_len = max(max_len,right-left+1)

    return max_len

#using set
def longestsubstrset(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):

        while s[right] in char_set:
            char_set.remove(s[left])
            left +=1

        char_set.add(s[right])

        max_len = max(max_len,right-left+1)

    print(max_len)

if __name__ == "__main__":
    s = "abcabcbb"
    # print(longestsubstr(s))
    longestsubstrset(s)