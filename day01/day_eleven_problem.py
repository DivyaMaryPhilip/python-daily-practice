"""Given a string s, find the length of the longest substring that contains at most one repeating character."""

def ret_longestsubarr(s):
    left = 0
    freq = {}
    rep_char=0
    max_len=0

    for right in range(len(s)):
        freq[s[right]]= freq.get(s[right],0)+1
        if freq[s[right]]==2:
            rep_char+=1

        while rep_char>1:   
            if freq[s[left]]==2:
                rep_char-=1
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1

        max_len = max(max_len,right-left+1)
    print(max_len)

if __name__ == "__main__":
    s = "chabhahla"
    ret_longestsubarr(s)