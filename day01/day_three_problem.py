"""Given an array of integers nums, return the first number that appears only once, preserving the original order.
If no such number exists, return -1
"""

def returnfirstnum(int_arr):
    freq={}
    for everynum in int_arr:
        freq[everynum] = freq.get(everynum,0)+1

    for everynum2 in int_arr:
        if freq[everynum2]==1:
            return everynum2
    return -1

if __name__ == "__main__":
    int_arr = [4,5,1,4,3]
    print(returnfirstnum(int_arr))