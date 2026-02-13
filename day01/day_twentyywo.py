"""Given an array of integers and an integer k, find the maximum sum of any contiguous subarray of size k."""

def lomgestsubarr(arr,k):
    left = 0 
    curr_win_sum = 0
    max_sum = 0

    for right in range(len(arr)):
        curr_win_sum += arr[right]

        if right-left+1 == k:
            max_sum = max(max_sum,curr_win_sum)
            curr_win_sum-=arr[left]
            left+=1
            
    print(max_sum)


if __name__ == "__main__":
    arr = [2,1,5,1,3,2]
    k = 3
    lomgestsubarr(arr,k)



