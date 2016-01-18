# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def prefix(A):
    n = len(A)
    Pa = [0]*(n)
    Pc = [0]*(n)
    Pg = [0]*(n)
    for k in xrange(n):
        if(A[k] == 'A'):
            Pa[k] = 1
        elif(A[k] == 'C'):
            Pc[k] = 1
        elif(A[k] == 'G'):
            Pg[k] = 1
        else:
            continue
    return Pa, Pc, Pg

def prefix_sums(A):
    n=len(A)
    P=[0]*(n+1)
    for k in xrange(1,(n+1)):
        P[k] = P[(k-1)] + A[(k-1)]
    return P

def solution(S, P, Q):
    m = len(P)
    Pa, Pc, Pg = prefix(S)
    print Pa, Pc, Pg
    SPa = prefix_sums(Pa)
    SPc = prefix_sums(Pc)
    SPg = prefix_sums(Pg)
    SOL=[]
    for i in xrange(m):
        if (SPa[(Q[i]+1)] - SPa[P[i]]) != 0:
            SOL.append(1)
        elif (SPc[(Q[i]+1)] - SPc[P[i]]) != 0:
            SOL.append(2)
        elif (SPg[(Q[i]+1)] - SPg[P[i]]) != 0:
            SOL.append(3)
        else:
            SOL.append(4)
    return SOL