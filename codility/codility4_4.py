def solution(N, A):
    P = [0] * N
    max_val = 0
    last_update = 0
    for i in A:
        if i < (N+1):
            if P[i-1] < last_update:
                P[i-1] = last_update

            P[i-1]+=1

            if P[i-1] > max_val:
                max_val = P[i-1]
        else:
            last_update = max_val

    for i in xrange(N):
        if P[i] < last_update:
            P[i] = last_update

    return P

print solution(5, [3,4,4,6,1,4,4])