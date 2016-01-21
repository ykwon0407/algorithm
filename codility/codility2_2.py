# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, K):
    # write your code in Python 2.7
    if K is 0 or A == []:
        return A
    else:
        N = len(A)
        B = [0]*N
        B[0] = A[-1]
        B[1:N] = A[0:(N-1)]
        return solution(B,K-1)


A=[]
K=3

print solution(A,K)
