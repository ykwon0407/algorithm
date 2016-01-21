# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    missing_int = 0
    for value in A:
        missing_int ^= value
    return missing_int

A= [2,2,1,3,3]
print solution(A)
