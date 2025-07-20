n,m= map(int,input().split())
l = []
def recu():
    if len(l)==m:
        print(*l)
        return
    for i in range(1,n+1):
        l.append(i)
        recu()
        l.pop()
recu()
