user=input("Please input something with space:")
mystr=''
mylist=[]
finallist=[]
for i in user:
    if i!=" ":
        mystr+=i
    else:
        mylist.append(int(mystr))
        mystr=''
mylist.append(int(mystr))
for i in mylist:
    if i%2!=0:
        finallist.append(i)
print(finallist)