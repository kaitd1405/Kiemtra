a = input()
k = int(input())
for i in range(k):
    ans = ""
    cnt = 1
    for j in range(1,len(a)):
        if (a[j]!=a[j-1]):
            ans+=str(cnt)+a[j-1]
            cnt = 1
        else:
            cnt+=1
    if (cnt!=0) :
        ans+=str(cnt)+a[len(a)-1]
    print(ans)
    a=ans
