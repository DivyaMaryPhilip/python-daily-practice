"""Given a string s, find the length of the longest substring without repeating characters."""

def longest_substr(s):
    freq = {}
    left = 0
    max_len=0
    startpoint = 0
    for right in range(len(s)):
        freq[s[right]]=freq.get(s[right],0)+1

        while freq[s[right]]>1:
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1

        if right-left+1>max_len:
            max_len = right - left + 1
            startpoint = left
    
    print(s[startpoint:startpoint+max_len])


if __name__ == "__main__":
    s = "ecebad"
    longest_substr(s)