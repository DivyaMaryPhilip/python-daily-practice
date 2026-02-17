"""Given a string s and an integer k, 
return the length of the longest substring that contains at most k distinct characters."""

def longestsubstr(s,k):
    #we will use dictionary to store the characters in string with the frequency of occurrence of each
    freq = {}
    left = 0
    max_len = 0

    #we will use a sliding window tecbique as this is a substring problem
    for right in range(len(s)):
        freq[s[right]]=freq.get(s[right],0)+1

    #if condition not met, ie. if the distinctive charcters in substring exceeds k, we will shrink the window
        while len(freq)>k:
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1

        max_len = max(max_len,right-left+1)

    return max_len


if __name__ == "__main__":
    s = "eceba"
    k = 0
    print(longestsubstr(s,k))