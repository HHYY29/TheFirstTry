t=int(input())
for i in range(t):
    n=int(input())
    a=list(input().split())
    a=[int(i) for i in a]
    a.sort()
    ans=0
    for j in range(1,n):
        ans+=a[j]-a[j-1]
    print(ans)
