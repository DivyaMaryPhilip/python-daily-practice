"""Given an array of integers nums, return the index of the first element whose frequency is exactly k.
If no such element exists, return -1."""

def returnind(nums,k):
    freq={}
    for everynum in nums:
        freq[everynum]=freq.get(everynum,0)+1
    
    for index,num in enumerate(nums):
        if freq[num]==k:
            return index
    return -1


if __name__=="__main__":
    nums = [7,1,7,5,8,5,2,3,2,8,1,8]
    k = 3
    print(returnind(nums,k))