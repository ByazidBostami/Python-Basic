user=input("Please input number with comma:")
mylist=user.split(",")
finallist=[]
modlist=[]
for i in mylist:
    finallist.append(int(i))
for i in finallist:
    if i not in modlist:
        modlist.append(i)
print(modlist)

