user=input("Please input something with comma:")
mystr=""
mylist=[]
for i in user:
    if i!=",":
        mystr+=i
    else:
        mylist.append(int(mystr))
        mystr=""

mylist.append(int(mystr))
print(mylist)
if len(mylist)<4:
    print("Not possible")
else:
    print(mylist[2:len(mylist)-2])
