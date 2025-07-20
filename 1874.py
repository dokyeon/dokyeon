n = int(input())
st = []
t = []
ans = []
for i in range(n):
    t.append(int(input()))
idx = 0
for i in range(1,n+1):
    st.append(i)
    ans.append("+")
    while len(st) > 0 and st[-1] == t[idx]:
        st.pop()
        ans.append('-')
        idx += 1
print(*ans,sep="\n")

    