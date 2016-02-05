def goldenleader(A):
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
    return leader, count


def solution(A):
    n = len(A)
    count = 0
    candidate, leader_count = goldenleader(A)
    if candidate == -1:
        return 0

    leader_count_so_far = 0
    for index in xrange(n):
        if A[index] == candidate:
            leader_count_so_far += 1
        if leader_count_so_far > (index+1)//2 and leader_count-leader_count_so_far > (n-index-1)//2:
            # Both the head and tail have leaders of the same value
            # as "leader"
            count += 1
    return count

print solution([1,2,3,4,5])
print solution([4,3,4,4,4,2])
