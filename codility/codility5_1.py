# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B, K):
    # write your code in Python 2.7
    return (A % K == 0) + ((B/K)-(A/K))

print solution(6,11,2)
