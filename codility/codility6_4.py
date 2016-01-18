def merge(A):
    n = len(A)
    P = []
    for i in range(n):
        P.append([(i-A[i]-0.1),i])
        P.append([(i+A[i]+0.1),i])
    return P

def solution(A):
    n = len(A)
    m = 2*n
    E =[x for [y,x] in sorted(merge(A))]
    print E

    count=0
    F=[[] for j in range(0,n)]
    for i in xrange(m):
        (F[E[i]]).append(i)
    print F

    for i in xrange(n):
        count += abs(F[i][0]-F[i][1])-1

    if count > 20000000:
        return -1
    return count/2


A = [3,10,3,2]
print solution(A)