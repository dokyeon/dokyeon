from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

q = deque()
n = int(input())
for _ in range(n):
    l = input().split()
    if l[0] == "push":
        q.append(l[1])
    elif l[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif l[0] == "size":
        print(len(q))
    elif l[0] == "empty":
        print(0 if q else 1)
    elif l[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif l[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)

