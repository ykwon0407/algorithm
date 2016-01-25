def prefix_sums(A):
    n=len(A)
    P=[0]*(n+1)
    for k in xrange(1,(n+1)):
        P[k] = P[(k-1)] + A[(k-1)]
    return P

def solution(A):
    P = prefix_sums(A)
    min = P[2]/2.0
    min_pos = 0
    for i in xrange(3, len(A)+1):
        temp = (P[i] - P[i-2]) / 2.0
        if temp < min:
            min = temp
            min_pos = i-2

        temp = (P[i] - P[i-3]) / 3.0
        if temp < min:
            min = temp
            min_pos = i-3

    return min_pos

print solution([4,1,2,2,4,8,4,4])