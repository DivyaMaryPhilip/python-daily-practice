"""Given a string s and an integer k, 
find the length of the longest substring that contains at most 
k distinct characters."""

def longestsubstr(s,k):
    freq = {}
    left = 0
    max_len = 0
    rep_char = 0

    for right in range(len(s)):
        freq[s[right]]=freq.get(s[right],0)+1
        rep_char = len(freq)

        while rep_char>k:
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1
            rep_char = len(freq)

        max_len = max(max_len,right-left+1)

    print(max_len)


if __name__ == "__main__":
    s = "eceba"
    k = 2
    longestsubstr(s,k)