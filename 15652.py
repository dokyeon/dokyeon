n,m = map(int, input().split())
l = []
def recu(a):
    if len(l)==m:
        print(*l)
        return
    for i in range(a, n+1):
        l.append(i)
        recu(i)
        l.pop()
recu(1)