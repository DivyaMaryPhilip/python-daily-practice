"""Given a string s, return True if it can become a palindrome after deleting at most one character."""

def palindrome_two(mystring):
    left_pointer = 0
    right_pointer = len(mystring)-1
    while left_pointer < right_pointer:
        if not mystring[left_pointer].isalnum():
            left_pointer+=1
            continue
        if not mystring[right_pointer].isalnum():
            right_pointer-=1
            continue
        if mystring[left_pointer] == mystring[right_pointer]:
            right_pointer-=1
            left_pointer+=1
        else:
            l = left_pointer+1
            r = right_pointer
            while l<r and mystring[l]==mystring[r]:
                l+=1
                r-=1
            if l>=r:
                return True
            
            l = left_pointer
            r=right_pointer-1
            while l<r and mystring[l]==mystring[r]:
                l+=1
                r-=1
            if l>=r:
                return True
            
            return False
    return True


if __name__ == "__main__":
    s = "ecbe"
    palindrome_two(s)


    if palindrome_two(s)==True:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
