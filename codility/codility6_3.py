# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    B = sorted(A)
    N = len(A)
    s0 = B[N-1]*B[N-2]*B[N-3]
    s1 = B[N-1]*B[0]*B[1]

    if s0 < s1:
        return s1
    else:
        return s0