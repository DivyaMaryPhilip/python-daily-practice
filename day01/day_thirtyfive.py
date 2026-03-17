"""Next Smaller Element to the Right- Given an array, for each element find the next smaller element to its right.
If none exists, return -1."""

def nextsmaller_ele_bruteforce(arr):

    res = []

    for i in range(len(arr)):
        found = False

        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                res.append(arr[j])
                found = True
                break

        if not found:
            res.append(-1)

    return res

def nextsmaller_stack(arr):
    result = []
    stack = []
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1]>=arr[i]:
            stack.pop()
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        
        stack.append(arr[i])

    return result[::-1]

        


if __name__ == "__main__":
    arr = [4,8,5,2,25]
    # print(nextsmaller_ele_bruteforce(arr))
    print(nextsmaller_stack(arr))