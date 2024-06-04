List_one =[1, 4, 7, 5]
List_two =[6, 1, 3, 9]
List_one[len(List_one)-1]=List_two[0]
for i in range(1,len(List_two)):
    List_one.append(List_two[i])
print(List_one)
