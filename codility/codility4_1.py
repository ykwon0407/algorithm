# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    T = range(1, N+1)
    try:
        for x in A:
            T[(x-1)] = 0

        if sum(T) is 0:
            return 1
        else:
            return 0
    except:
        return 0


print solution([4,1,3,2])
print solution([4,1,3])