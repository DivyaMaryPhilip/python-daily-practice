"""Given a string s and an integer k, return the longest substring that contains at most k distinct characters."""

def longest_substr(s,k):
    left = 0 
    freq = {}
    max_len = 0
    rep_char = 0
    start_point = 0

    for right in range(len(s)):
        freq[s[right]]=freq.get(s[right],0)+1
        rep_char = len(freq)

        while rep_char>k:
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1
            rep_char = len(freq)
        
        if right-left+1 > max_len:
            max_len = right-left+1
            start_point = left
    
    print(s[start_point:start_point+max_len])


if __name__ == "__main__":
    s = "eceba"
    k = 2
    longest_substr(s,k)