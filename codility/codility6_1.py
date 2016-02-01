# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    B = sorted(A)
    N = len(A)
    count =0
    for i in xrange(N-1):
        if B[i] == B[i+1]:
            count += 1

    return N-count

print solution([2,1,1,2,3,1])
