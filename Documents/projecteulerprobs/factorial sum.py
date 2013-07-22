def fact(n):
    ans=n
    while n>1:
        ans*=(n-1)
        n-=1
    return ans

ans=0
for c in str(fact(100)):
    ans+=int(c)

print ans
