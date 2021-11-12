n = int(input())
a = list(map(int,input().split()))
ans = []
for i in a :
    sum = 0
    j = 1
    while(j*j<=i) :
        if (i%j==0) :
            sum+=j
            if (i/j!=j) :
                sum+=(i/j)
        j+=1
    print(sum)
    if (sum-i>i) :
        ans.append(i)
print(len(ans))
print(sorted(ans))
