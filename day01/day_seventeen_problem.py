"""Given a string s and an integer k, find the length of the longest 
substring that can be obtained by replacing at most k characters, 
such that the substring contains only one repeating character."""

def repcharac(s,k):
    freq={}
    left = 0
    max_freq = 0
    max_len=0
    for right in range(len(s)):
        freq[s[right]]=freq.get(s[right],0)+1

        max_freq = max(max_freq,freq[s[right]])
    
        while right-left+1 - max_freq > k:
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1

        max_len = max(max_len,right-left+1)
    print(max_len)


if __name__ == "__main__":
    s = "aababba"
    k=1
    repcharac(s,k)