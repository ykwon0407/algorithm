# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    B = sorted(A)
    N = len(A)
    for i in xrange(N-2):
        if B[i] + B[i+1] > B[i+2]:
            return 1
    return 0