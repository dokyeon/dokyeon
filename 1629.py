A, B, C = map(int,input().split())

def pow(a, b, c):
    if b == 1: return a%c
    if b%2 == 0:
        return pow(a, b//2,c) ** 2 % c
    else:
        return pow(a, b//2, c) ** 2 % c * a % c

print(pow(A,B,C))
    