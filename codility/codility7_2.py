def solution(A, B):
    alive_count = 0
    downstream = []
    downstream_count = 0

    for index in xrange(len(A)):
        # Compute for each fish
        if B[index] == 1:
            downstream.append(A[index])
            downstream_count += 1
        else:
            while downstream_count != 0:
                if downstream[-1] < A[index]:
                    downstream_count -= 1
                    downstream.pop()
                else:
                    break
            else:
                alive_count += 1

    alive_count += len(downstream)

    return alive_count

print solution([4,3,2,1,5],[0,1,0,0,0])