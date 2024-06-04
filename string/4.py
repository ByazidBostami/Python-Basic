sum=0
for i in range(600):
    if i%7==0 and i%9==0 :
        sum-=i
    if i%7==0 or i%9==0:
        sum+=i
print(sum)