"""Next Greater Element (Intro to Monotonic Stack)
Given an array, return an array where each element contains the next greater element to its right.
"""

def nextgreater(arr):
    stack = []
    result_arr = [-1] * len(arr)
    for ele in range(len(arr)-1,-1,-1):
        while stack and arr[ele]>stack[-1]:
            stack.pop()
        if stack:
            result_arr[ele] = stack[-1]
        stack.append(arr[ele])
    return result_arr

if __name__=="__main__":
    arr = [2,1,2,4,3]
    print(nextgreater(arr))