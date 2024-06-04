user=input("Please input somethig with comma :")
mylist=user.split(",")
finallist=[]
for i in mylist:
    finallist.append(int(i))
maxi=finallist[0]
index=0
for i in range(len(finallist)):
    if finallist[i]>maxi:
        maxi=finallist[i]
        index=i
print(f"My list={finallist} \nLargest number in the list is {maxi} which was found at index:{index}")
