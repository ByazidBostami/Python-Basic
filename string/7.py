sum=0
count=0
for i in range(10):
    user=int(input("please input a number :"))
    if user%2!=0:
        count+=1
        sum=sum+user
        
print("The total of odd number is ",sum,"And the avarage is ",sum/count)