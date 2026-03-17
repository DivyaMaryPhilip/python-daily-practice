"""Given a string s and an integer k, return the longest substring that can be 
obtained by replacing 
at most k characters such that all characters in the substring are the same."""

def longestsubstr(s,k):
    left = 0
    freq = {}
    max_len = 0 
    max_freq = 0
    start = 0

    for right in range(len(s)):
        freq[s[right]]=freq.get(s[right],0)+1
        max_freq = max(max_freq,freq[s[right]])

        while right-left+1 - max_freq > k:
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1

        if right - left + 1 > max_len:
            max_len = right-left+1
            start = left

    print(s[start:start+max_len])


if __name__ == "__main__":
    s= "AAPABBA"
    k=1
    longestsubstr(s,k)