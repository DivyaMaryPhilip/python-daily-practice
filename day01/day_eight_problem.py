"""Given an integer array nums, return the length of the longest subarray that contains all unique elements."""


def return_subarr_len(numsarr):
    myset = set()
    left = 0
    max_len=0
    for right in range(len(numsarr)):
        while numsarr[right] in myset:
            myset.remove(numsarr[left])
            left+=1
        myset.add(numsarr[right])
        max_len = max(max_len,right-left+1)
    print(max_len)


if __name__ == "__main__":
    numsarr=[2,3,1,3,4,5,8,2]
    return_subarr_len(numsarr)