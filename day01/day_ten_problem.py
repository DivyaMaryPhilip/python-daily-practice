"""Given an array of positive integers nums and an integer k,
find the length of the longest contiguous subarray whose sum is less than or equal to k"""

def longest_subarr_len(num,k):
    sum=0
    left=0
    max_len=0
    for right in range(len(num)):
        sum+=num[right]
        while sum>k:
            sum-=num[left]
            left+=1
        max_len=max(max_len,right-left+1)
    print(max_len)


if __name__ == "__main__":
    num = [2,1,5,1,3,2]
    k = 7
    longest_subarr_len(num,k)