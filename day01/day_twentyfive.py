"""Given two strings s and t, return the minimum window substring of s 
such that every character in t (including duplicates) is included in the window.
If no such substring exists, return ""."""

def minsubstr(s,t):
    freq_s = {}
    freq_t = {}
    left = 0
    min_win = float('inf')
    start = 0
    counter = 0

    for right in range(len(t)):
        freq_t[t[right]]=freq_t.get(t[right],0)+1

    for right in range(len(s)):
        freq_s[s[right]]=freq_s.get(s[right],0)+1

        if s[right] in freq_t and freq_s[s[right]]==freq_t[s[right]]:
            counter+=1

        while counter == len(freq_t):

            if right-left+1<min_win:
                min_win=right-left+1
                start = left

            freq_s[s[left]]-=1

            if s[left] in freq_t and freq_s[s[left]]<freq_t[s[left]]:
                counter-=1

            if freq_s[s[left]]==0:
                del freq_s[s[left]]

            left+=1

    print(s[start:start+min_win])

if __name__ == "__main__":
    s = "AABBCCD"
    t = "ABC"
    minsubstr(s,t)