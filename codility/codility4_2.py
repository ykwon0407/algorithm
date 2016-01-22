# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    # write your code in Python 2.7
    count = 0
    T=[-1]*X
    for index, element in enumerate(A):
        if T[element-1] == -1:
            T[element-1] = element
            count += 1
            if count == X:
                return index
    return -1
