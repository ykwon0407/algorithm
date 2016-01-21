# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, Y, D):
    # write your code in Python 2.7
    return (Y-X)/D + ((Y-X) % D > 0)

X=10
Y=85
D=30

print solution(X,Y,D)