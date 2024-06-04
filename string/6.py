user=int(input("please input a number "))
sum=0
for i in range(user+1):
    if i%2==0:
        sum+=i**2*(-1)
    else:
        sum+=i**2
print(sum)
#or use this (i**2+(i+j)*(-1)**j