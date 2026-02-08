"""Given a string s, find the length of the longest substring that contains at most k distinct characters."""

def length_subset(s,k):
    left = 0
    freq={}
    max_len=0
    for right in range(len(s)):
        freq[s[right]]=freq.get(s[right],0)+1
        while len(freq)>k:
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1
        max_len=max(max_len,right-left+1)
    print(max_len)

if __name__ == "__main__":
    s = "eceba"
    k=2
    length_subset(s,k)