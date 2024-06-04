user=input("please input number with comma")
listone=user.split(",")
length=len(listone)
mylist=[]
for i in range(2,length-1,-1):
    mylist.append(int(user(i)))
print(i)