# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    T = [0]*N
    for index, element in enumerate(A):
        if element > len(A) or element < 1:
            continue
        else:
            T[element-1] = 1

    if sum(T) == N:
        return (N+1)
    else:
        for i in xrange(N):
            if T[i] == 0:
                return (i+1)

