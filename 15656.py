n,m = map(int, input().split())
l = list(map(int,input().split()))
l.sort()
ans = []
def recu(a):
    if len(ans)==m:
        print(*l)
        return
    for i in range(a, n+1):
        if l[i] == -1:
            continue
        ans.append(i)
        l[i] = -1
        recu(i)
        ans.pop()
recu(1)