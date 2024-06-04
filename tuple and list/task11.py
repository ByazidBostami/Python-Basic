List_one =[1, 4, 3, 2, 6]
List_two =[5, 6, 9, 8, 7]
flag=False
for i in List_one:
    for j in List_two:
        if i==j:
            flag=True
if flag==True:
    print("True")    
else:
    print("False")    

