list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]
newlist=list_one+list_two
finallist=[]
for i in newlist:
    if i%2==0:
        finallist.append(i)
print(finallist)