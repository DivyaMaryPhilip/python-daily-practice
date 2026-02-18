"""Given a string s, return True if it is a palindrome, 
considering only alphanumeric characters and ignoring cases. Otherwise return False"""

def palindrome(s):
    right = len(s)-1
    left = 0

    while left<right:
        if s[left].isalnum() and s[right].isalnum():
            if s[left].lower()==s[right].lower():
                right-=1
                left+=1
            else:
                return False
        elif not s[left].isalnum():
            left+=1
        else:
            right-=1
    return True

if __name__ == "__main__":
    s = "nanan"
    result = palindrome(s)

    if result == True:
        print("It is palindrome")
    else:
        print("It is not palindrome")