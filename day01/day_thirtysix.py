"""Given daily stock prices, calculate the span of the stock’s price for each day.

The span is the number of consecutive days (including today) where the price was less than or equal to today's price."""

def generate_span(arr):
    stack = []
    span = [0]*len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]]<=arr[i]:
            stack.pop()
        if not stack:
            span[i]=i+1
        else:
            span[i]=i-stack[-1]
        stack.append(i)
    return span

if __name__ == "__main__":
    arr = [100,80,60,70,60,75,85]
    print(generate_span(arr))