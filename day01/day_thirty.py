"""Given a string containing:
lowercase letters
parentheses: ( ) { } [ ]
Return True if parentheses are valid.
Ignore letters."""

def valid_check(s):
    stack=[]
    mydict = {
        ")"  :  "(",
        "]"  :  "[",
        "}"  :  "{"
    }
    for char in s:
        if char in mydict.values():
            stack.append(char)
        elif char.isalnum():
            continue
        elif char in mydict:
            if not stack or stack[-1]!=mydict[char]:
                return False
            stack.pop()

    return len(stack)==0

if __name__ == "__main__":
    s = "s(b)c)"
    valid_check(s)

    if valid_check(s):
        print("Valid")
    else:
        print("Invalid")
