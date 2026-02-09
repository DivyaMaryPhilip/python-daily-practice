"""Longest substring with at most K distinct characters"""

def large_substr(s,k):
    freq = {}
    left=0
    dist_char = 0
    max_len = 0
    start = 0

    for right in range(len(s)):
        freq[s[right]]=freq.get(s[right],0)+1
        dist_char=len(freq) # Tracking unique alphabets
        

        while dist_char>k:  # if more than 2 then slide the left pointer to right
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1
            dist_char = len(freq)        

        if right-left+1>max_len:
            max_len = right-left+1
            start = left

    
    print(s[start:start+max_len])


if __name__ == "__main__":
    s = "eceba"
    k=2
    large_substr(s,k)
