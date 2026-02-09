"""Given a string s and an integer k, find the length of the longest substring that contains at most k distinct characters."""

def len_longsubstr_k(s,k):
    left = 0
    max_len= 0
    freq={}
    dist_charac=0

    for right in range(len(s)):
        freq[s[right]]=freq.get(s[right],0)+1
        dist_charac = len(freq)

        while dist_charac>k:
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1
            dist_charac=len(freq)

        max_len = max(max_len,right-left+1)
    print(max_len)

if __name__=="__main__":
    s="eceba"
    k=2
    len_longsubstr_k(s,k)