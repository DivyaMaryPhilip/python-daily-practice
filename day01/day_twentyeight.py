"""Given a string containing only:( ) { } [ ].  ;   Return True if the string is valid."""

def valiparantheseis(s):
    stack = []
    mapping = {
        ')' : '(' ,
        '}' : '{' ,
        ']' : '[' 
    }

    for char in s:
        if char in mapping.values():
            stack.append(char)

        elif char in mapping:
            if not stack or stack[-1]!=mapping[char]:
                return False
            stack.pop()

        else:
            return False      
    return len(stack)==0


if __name__ == "__main__":
    s = "((("
    valiparantheseis(s)

    if valiparantheseis(s):
        print("Valid")
    else:
        print("Invalid")