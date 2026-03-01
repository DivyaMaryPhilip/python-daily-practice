"""Given an array, for each element find the next greater element to its right.
If none exists, return -1."""

def greater_ele(arr):
    stack = []
    for i in range(len(arr)):

        found = False
        
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                stack.append(arr[j])
                found = True
                break
        if not found:
            stack.append(-1)                 
    return stack

def greater_ele_stack(arr):
    stack = []
    result=[]

    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1]<=arr[i]:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(arr[i])

    return result[::-1]

if __name__ == "__main__":
    arr = [4,5,9,10]
    print(greater_ele_stack(arr))