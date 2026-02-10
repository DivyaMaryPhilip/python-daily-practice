"""Given a string s, find the length of the longest substring that contains at most 2 distinct characters."""

def longestdictsubstr(s):
    freq={}
    left = 0
    dist_char = 0
    max_len=0
    for right in range(len(s)):
        freq[s[right]]=freq.get(s[right],0)+1
        dist_char=len(freq)

        while dist_char>2:
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1
            dist_char=len(freq)
        
        max_len= max(max_len,right-left+1)
    print(max_len)

if __name__=="__main__":
    s = "abbadef"
    longestdictsubstr(s)