# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    T = range(1, N+2)
    for x in A:
        T[(x-1)] = 0

    return sum(T)

A = [2,3,1,5]
print solution(A)
