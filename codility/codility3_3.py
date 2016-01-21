# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    dist = 2*A[0]-sum(A)
    best = abs(dist)
    count = 0
    for x in A:
        if count == 0 or count == (len(A)-1):
            count += 1
            continue
        else:
            count += 1
            dist += 2*x
            if best > abs(dist):
                best = abs(dist)
    return best


print solution([3,1,2,4,3])
print solution([-1000,1000])
