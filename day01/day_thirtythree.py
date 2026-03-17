"""Given an array representing heights of bars in a histogram, find the area of the largest rectangle that can be formed"""

def large_rectangle(arr):
    max_area = 0
    for height in range(len(arr)):
        curr_height = arr[height]
        left=height
        while left>=0 and curr_height<=arr[left]:
            left-=1

        right=height
        while right<len(arr) and curr_height<=arr[right]:
            right+=1

        width = right - left - 1
        area=curr_height*width

        max_area = max(area, max_area)

    print(max_area)

def large_rect_stack(arr):
    max_area = 0
    stack = []
    for height in arr:
        curr_height = arr[height]
        while stack and curr_height>arr[height]:
            height = arr[stack.pop()]

            if stack:
                width = height - stack[-1]-1
            else:
                width = height

            area = height * width
            max_area = max(max_area,area)

        stack.append(height)

        while stack:
            height = arr[stack.pop()]

            if stack:
                width = len(arr) - stack[-1]-1
            else:
                width = len(arr)

            area = len(arr) * width
            max_area = max(area,max_area)


if __name__ == "__main__":
    arr = [2,1,5,6,2,3]
    large_rectangle(arr)
