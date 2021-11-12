a = input()
b = input()
ans = 0
for i in range(len(b)):
    ans+=b.count(a,i,i+len(a))
print(ans)