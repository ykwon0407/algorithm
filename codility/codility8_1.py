def solution(A):
    n = len(A)
    if n == 0:
        return -1
    size = 0
    for k in xrange(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if value != A[k]:
                size -= 1
            else:
                size += 1
        candidate = -1

    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    for k in xrange(n):
        if (A[k] == candidate):
            ind = k
            count += 1

    if (count > n // 2):
        leader = candidate
        return ind
    else:
        return -1


print solution([0,0,1,1,1])

