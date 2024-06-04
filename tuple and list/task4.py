mystr=""
mylist=[]
myfinallist=[]
user=input("Please input something ")
for i in user:
    if i !=",":
        mystr+=i
    else:
        mylist.append(int(mystr))
        mystr=""
mylist.append(int(mystr))
for i in mylist:
    myfinallist.append(i*i)
print(myfinallist)