# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    # write your code in Python 2.7
    bin_N = bin(N)[2:]
    M = len(bin_N)
    gap = 0
    old = 0
    for i in xrange(M):
        if i == 0:
            new = 0
        else:
            if int(bin_N[i]) == 1:
                new = i
                if (new - old-1) > gap:
                    gap = new - old-1
                old = i

    return gap
