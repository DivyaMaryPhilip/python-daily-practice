"""Given two strings s and t, return the minimum window substring of s
such that every character in t (including duplicates) is included in the window."""

def min_win(s,t):
    freq_t = {}
    freq = {}
    left = 0
    min_length = float('inf')
    count  = 0
    start = 0 
    
    for ch in range(len(t)):
        freq_t[t[ch]] = freq_t.get(t[ch],0)+1

    for right in range(len(s)):
        freq[s[right]]=freq.get(s[right],0)+1

        if s[right] in freq_t and freq[s[right]] == freq_t[s[right]]:
            count += 1

        while count == len(freq_t):
            if right-left+1 < min_length:
                min_length = right-left+1
                start = left

            freq[s[left]]-=1
            if s[left] in freq_t and freq[s[left]] < freq_t[s[left]]:
                count-=1

            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1 
    
    if min_length == float('inf'):
        print("")
    else:
        print(s[start:start+min_length])

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    min_win(s,t)