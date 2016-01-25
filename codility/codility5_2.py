def prefix_sums(A):
    n=len(A)
    P=[0]*(n+1)
    for k in xrange(1,(n+1)):
        P[k] = P[(k-1)] + A[(k-1)]
    return P

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    P = prefix_sums(A)
    count = 0
    for ind, x in enumerate(A):
        if x == 1:
            continue
        else:
            count += (P[len(A)]-P[ind+1])
            if count > 10 ** 9:
                return -1
    return count

print solution([0,1,0,1,1])