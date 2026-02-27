"""Given a string, repeatedly remove adjacent duplicates"""

def rem_repchar(s):
    stack = []
    for item in s:
        if stack and item==stack[-1]:
            stack.pop()
        else:
            stack.append(item)
    return ''.join(stack)
    # print(stack)


if __name__ == "__main__":
    s = "aabbca"
    rem_repchar(s)
    print(rem_repchar(s))