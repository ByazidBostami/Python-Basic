mylist=[]
for i in range(5):
    user=int(input())
    mylist.append(user)
print(mylist)
for i in range(len(mylist)-1,-1,-1):
    print(mylist[i])