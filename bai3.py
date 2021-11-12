n = int(input())
a = list(map(int,input().split()))
cnt = 0 
for i in a:
    j = 1
    dem=0
    while(j*j<=i):
        if (i%j==0) :
            dem+=1
            if (i/j!=j):
                dem+=1
        j+=1
    if (dem==3) :
        cnt+=1
print(cnt)