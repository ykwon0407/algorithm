def push(x):
    global stack, size
    stack[size] = x
    size += 1

def pop(x):
    global stack, size
    if stack[size-1] == -x:
        stack[size-1] = 0
        size -= 1
    else:
        return 1/0

def change(S):
    B = [0]*len(S)
    for i, x in enumerate(S):
        if x == '(':
            B[i] = 1
        elif x == '{':
            B[i] = 2
        elif x == '[':
            B[i] = 3
        elif x == ')':
            B[i] = -1
        elif x == '}':
            B[i] = -2
        else:
            B[i] = -3
    return B

def solution(S):
    if S == '':
        return 1
    B = change(S)
    global stack, size
    stack = [0]*len(B)
    size = 0
    if sum(B) != 0 or B[0] < 0:
        return 0
    try:
        for x in B:
            if x > 0:
                push(x)
            else:
                pop(x)
    except:
        return 0

    if size == 0:
        return 1
    else:
        return 0


print solution('')

